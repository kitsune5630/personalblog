from django.db import models

# put there for auto html generation plus db generation

class PostsModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    

