# from django.contrib.auth.models import User
from django.db import models
from author.models import AppUser
from kudos.model import BaseModal


class Blog(BaseModal):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, blank=True)
    short_content = models.CharField(max_length=50)
    author = models.ManyToManyField(AppUser, related_name="authors")
    number_of_kudos = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    published_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:30]


class Content(BaseModal):
    id = models.AutoField(primary_key=True)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.content[:30]