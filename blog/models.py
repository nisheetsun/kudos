# from django.contrib.auth.models import User
from django.db import models
from author.models import AppUser
from kudos.model import BaseModal

# Create your models here.

class Blog(BaseModal):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=30)
    author = models.ManyToManyField(AppUser, related_name="authors")
    number_of_kudos = models.PositiveIntegerField()
    number_of_articles = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=0)
    published_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=0)

class Content(BaseModal):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

# class Kudos(BaseModal):
#     user = User()

# class Flaged(BaseModal):
#     user = User()
