from rest_framework import serializers
from .models import AppUser
from django.contrib.auth.models import User

# from blog.serializers import BlogSerializerKudos
# try:
#     from blog.serializers import BlogSerializerKudos
# except ImportError:
#     import sys
#     BlogSerializerKudos = sys.modules[__package__ + '.BlogSerializerKudos']


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AppUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class AuthorBlogSerializer(serializers.ModelSerializer):
    # from blog.serializers import BlogSerializerKudos
    id = serializers.IntegerField(read_only=True)
    # blogs = BlogSerializer(read_only=True)
    class Meta:
        model = AppUser
        fields = '__all__'