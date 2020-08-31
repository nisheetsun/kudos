from .models import Blog, Content
from author.models import AppUser
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BlogSerializer, ContentSerializer, BlogSerializerUpdate
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import BlogPermission



class ContentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    renderer_classes = [JSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        content = get_object_or_404(self.queryset, blog=kwargs['pk'])
        serializer = self.serializer_class(content)
        return JsonResponse(serializer.data, safe=True)



class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [BlogPermission]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def get_queryset(self):
        if self.action == 'list':
            if self.request.query_params.get('filter') == 'draft':
                if self.request.user.is_superuser:
                    # return draft blog by all users
                    return Blog.objects.filter(is_private=True, is_published=False)
                return Blog.objects.filter(is_private=True, author__parent_user__id__in=[self.request.user.id])
            if self.request.query_params.get('filter') == 'waiting':
                if self.request.user.is_staff or self.request.user.is_superuser:
                    # return waiting to be published blog by all users
                    return Blog.objects.filter(is_private=False, is_published=False)
                return Blog.objects.filter(is_private=False, author__parent_user__id__in=[self.request.user.id], is_published=False)
            return Blog.objects.filter(is_private=False, is_published=True)
        return Blog.objects.all()

    def list(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).list(request, *args, **kwargs)
        response.template_name='list.html'
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).retrieve(request, *args, **kwargs)
        response.template_name='content.html'
        return response

    def create(self, request, *args, **kwargs):
        request.data['author_list'].append(request.user.id)
        response = super(BlogViewSet, self).create(request, *args, **kwargs)
        return response
    
    def partial_update(self, request, *args, **kwargs):
        if 'author_list' in request.data:
            request.data['author_list'].append(request.user.id)
        response = super(BlogViewSet, self).partial_update(request, *args, **kwargs)
        return response

    @action(detail=True, methods=['get'])
    def edit_post(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.serializer_class(blog)
        template = 'edit.html'
        data = {'serializer': serializer, 'id': blog.id}
        if request.accepted_renderer.format == 'html':
            return Response(data, template_name=template)

    @action(detail=True, methods=['post'])
    def give_kudos(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
        data = blog.__dict__
        data['number_of_kudos'] = data['number_of_kudos'] + 1
        serializer = BlogSerializerUpdate(blog, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    @action(detail=True, methods=['post'])
    def publish(self, request, *args, **kwargs):
        blog = self.get_object()
        data = blog.__dict__
        data['is_published'] = True
        serializer = BlogSerializerUpdate(blog, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    @action(detail=True, methods=['post'])
    def unpublish(self, request, *args, **kwargs):
        blog = self.get_object()
        data = blog.__dict__
        data['is_published'] = False
        serializer = BlogSerializerUpdate(blog, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    @action(detail=False, methods=['get'])
    def create_blog(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer}, template_name='post.html')


    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
