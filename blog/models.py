# from django.contrib.auth.models import User
from django.db import models
from author.models import AppUser
from kudos.model import BaseModal


class Blog(BaseModal):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, blank=True)
    short_content = models.CharField(max_length=50)
    author = models.ManyToManyField(AppUser, related_name="authors")
    number_of_kudos = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=0)
    published_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True)
    is_private = models.BooleanField(default=0)


class Content(BaseModal):
    id = models.IntegerField(primary_key=True)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, blank=True)

# class Kudos(BaseModal):

# class Flaged(BaseModal):
