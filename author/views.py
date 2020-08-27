from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets, mixins
from .models import AppUser
from blog.models import Blog
from .serializers import AuthorSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .temp import AuthorBlogSerializer
from blog.serializers import BlogSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AuthorSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    
    class Meta:
        ordering = ['-id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorBlogSerializer
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        response = super(AuthorViewSet, self).list(request, *args, **kwargs)
        response.template_name='author_list.html'
        return response
    
    @action(detail=False, methods=['get'])
    def authors_except_self(self, request, *args, **kwargs):
        response = super(AuthorViewSet, self).list(request, *args, **kwargs)
        for data in response.data['results']:
            if data['parent_user'] == request.user.id:
                response.data['results'].remove(data)
        return response
    
    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(AppUser, pk=kwargs['pk'])
        blogs = Blog.objects.filter(author__id = kwargs['pk'])
        user.blog_set.set(blogs)
        serializer = AuthorBlogSerializer(instance=user)
        return Response(serializer.data, template_name='author_detail.html')
