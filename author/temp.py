from rest_framework import serializers
from .models import AppUser
from blog.serializers import BlogSerializer
from .serializers import UserSerializer

# solve import error and  move to author/serializers.py
class AuthorBlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    blogs = BlogSerializer(read_only=True, many=True, source='blog_set')
    user_details = UserSerializer(source='parent_user')
    class Meta:
        model = AppUser
        fields = '__all__'