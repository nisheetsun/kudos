from .models import Blog, Content
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BlogSerializer, ContentSerializer, BlogSerializerKudos
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from django.http import JsonResponse


class ContentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    renderer_classes = [JSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        content = get_object_or_404(self.queryset, blog=kwargs['pk'])
        serializer = self.serializer_class(content)
        return JsonResponse(serializer.data, safe=True)



class BlogViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='list.html')
        return response

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == 'post_new_blog':
            # can a seperate view
            serializer = self.get_serializer()
            template = 'post.html'
            data = {'serializer': serializer}
        else:
            response = super(BlogViewSet, self).retrieve(request, *args, **kwargs)
            # move this to class variable
            template = 'content.html'
            data = response.data
        if request.accepted_renderer.format == 'html':
            return Response(data, template_name=template)
        return response

    def create(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).create(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            redirect_url = '/blog/' + str(response.data['id']) + '/'
            return redirect(redirect_url)

    @action(detail=True, methods=['get', 'post'])
    def edit_post(self, request, *args, **kwargs):
        if request.method == "POST":
            blog = get_object_or_404(Blog, pk=kwargs['pk'])
            serializer = self.serializer_class(blog, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if request.accepted_renderer.format == 'html':
                redirect_url = '/blog/' + kwargs['pk']
                return redirect(redirect_url)
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
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
        serializer = BlogSerializerKudos(blog, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)


    def destroy(self, request, pk=None):
        # wip
        return Response({})
