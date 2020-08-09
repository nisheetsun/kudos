from django.db import models
from django.contrib.auth.models import User as DefaultUserModal
from kudos.model import BaseModal

# Create your models here.

class AppUser(BaseModal):
    user = models.OneToOneField(DefaultUserModal, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    number_of_articles = models.PositiveIntegerField(default=0)