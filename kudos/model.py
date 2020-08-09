from django.db import models
# from django.contrib.auth.models import User

class BaseModal(models.Model):
    date_creatd = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True