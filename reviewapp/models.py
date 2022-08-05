from django.db import models
from accountapp.models import User

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    categories = models.JSONField(default=list)
    region = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100, null=True)
