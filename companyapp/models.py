# from django.contrib.postgres.fields import ArrayField
from django.db import models
from accountapp.models import User

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    categories = models.JSONField(default=list)
    region = models.IntegerField()
    phone = models.CharField(max_length=100)   # todo: 폰번호 저장 형식
    siteUrl = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name="companies", on_delete=models.SET_NULL, null=True)
