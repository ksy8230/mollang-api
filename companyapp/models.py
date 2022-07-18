# from django.contrib.postgres.fields import ArrayField
from django.db import models
# from django.contrib.postgres.fields import JSONField

# Create your models here.
from accountapp.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    categories = models.JSONField()
    region = models.IntegerField()
    phone = models.CharField(max_length=100) # todo 폰번호 저장 형식
    siteUrl = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='company', null=True)


