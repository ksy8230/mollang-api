from django.db import models


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.JSONField(default=list)
    region = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100, null=True)
