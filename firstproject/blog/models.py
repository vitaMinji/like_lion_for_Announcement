from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    updated_date = models.DateTimeField(auto_now_add=True)
    body=models.TextField()