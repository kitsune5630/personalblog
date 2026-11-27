from django.contrib import admin
from .models import PostsModel, CommentModel, ProfileModel

# Register your models here.

admin.site.register(PostsModel)
admin.site.register(CommentModel)
admin.site.register(ProfileModel)