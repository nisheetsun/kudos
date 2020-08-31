from rest_framework import serializers
from .models import Blog, Content
from author.serializers import AuthorSerializer
from author.models import AppUser


class ContentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Content
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField(write_only=True, style={'base_template': 'textarea.html', 'rows': 10}, allow_blank=True, required=True)
    number_of_kudos = serializers.IntegerField(default=0, read_only=True)
    author = AuthorSerializer(many=True, read_only=True)
    author_list = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Blog
        exclude = ['published_by']

    def create(self, validated_data):
        content_data = validated_data.pop('content', '')
        author_list = validated_data.pop('author_list', '')
        authors = AppUser.objects.filter(id__in=author_list)
        blog = Blog(title=validated_data['title'],
            image_url=validated_data['image_url'],
            short_content=validated_data["short_content"],
            is_private=validated_data["is_private"])
        blog.save()
        for author in authors:
            blog.author.add(author)
        content = ContentSerializer(data={'blog': blog.id, 'content': content_data})
        content.is_valid(raise_exception=True)
        content.save()
        return blog
    
    def update(self, instance, validated_data):
        content_data = validated_data.pop('content', False)
        author_list = validated_data.pop('author_list', [])
        authors = AppUser.objects.filter(id__in=author_list)
        validated_data['is_published'] = False
        blog = super(BlogSerializer, self).update(instance, validated_data)
        for author in authors:
            blog.author.add(author)
        if content_data:
            content_data = {'blog': blog.id, 'content': content_data}
            content = Content.objects.get(blog__id=blog.id)
            serializer = ContentSerializer(content, data=content_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return blog

# This serializer exists because content and author_list is not required here.
class BlogSerializerUpdate(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
