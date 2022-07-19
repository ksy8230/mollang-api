# from django.contrib.postgres.fields import ArrayField
from django.db import models
# from django.contrib.postgres.fields import JSONField

# Create your models here.
from accountapp.models import User
# from django.contrib.auth.models import User
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    categories = models.JSONField()
    region = models.IntegerField()
    phone = models.CharField(max_length=100) # todo 폰번호 저장 형식
    siteUrl = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100, null=True)
    # user = models.ForeignKey(User, related_name="companies", on_delete=models.SET_NULL, null=True)


