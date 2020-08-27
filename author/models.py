from django.db import models
from django.contrib.auth.models import User as DefaultUserModal
from kudos.model import BaseModal

# Create your models here.

class AppUser(BaseModal):
    id = models.IntegerField(primary_key=True)
    parent_user = models.OneToOneField(DefaultUserModal, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    number_of_articles = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.alias_name