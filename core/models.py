from django.db import models

# put there for auto html generation plus db generation

class UserModel(models.Model):
    username = models.CharField(
        unique=True, 
    )
    password = models.CharField()
    email = models.CharField(
        unique=True, 
    )

class PostsModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_att = models.DateTimeField(auto_now_add=True)

