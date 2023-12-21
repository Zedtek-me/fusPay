from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class BasicCrud(models.Model):
    name = models.CharField(max_length=2000, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name