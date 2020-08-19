from rest_framework import serializers
from .models import Blog, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(style={'base_template': 'textarea.html'})
    content = serializers.CharField(write_only=True)
    number_of_kudos = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Blog
        exclude = ['is_published', 'published_by', 'is_private']

    def create(self, validated_data):
        content_data = validated_data.pop('content', '')
        blog = super(BlogSerializer, self).create(validated_data)
        content = ContentSerializer(data={'blog': blog.id, 'content': content_data})
        content.is_valid(raise_exception=True)
        content.save()
        return blog
