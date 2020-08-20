from rest_framework import serializers
from .models import Blog, Content


class ContentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Content
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField(write_only=True, style={'base_template': 'textarea.html', 'rows': 10}, allow_blank=True)
    number_of_kudos = serializers.IntegerField(default=0, read_only=True)
    # author = serializers.IntegerField(AppUser, related_name="authors")

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
    
    def update(self, instance, validated_data):
        _content = validated_data.pop('content', '')
        blog = super(BlogSerializer, self).update(instance, validated_data)
        content = Content.objects.get(blog=blog)
        content_data = {'blog': blog.id, 'content': _content}
        serializer = ContentSerializer(content, data=content_data)
        serializer.is_valid()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return blog

class BlogSerializerKudos(serializers.ModelSerializer):
    number_of_kudos = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Blog
        fields = ['number_of_kudos']
