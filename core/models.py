from django.db import models
from django.utils.text import slugify

# put there for auto html generation plus db generation

class PostsModel(models.Model):
    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

