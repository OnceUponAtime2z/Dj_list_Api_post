from turtle import title
from django.db import models

    
class Api(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_Id = models.CharField(max_length=10)
    title = models.TextField()
    body = models.TextField()
    
    def __str__(self):
        return self.name
    
