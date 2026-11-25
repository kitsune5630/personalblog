from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    PostsModel = apps.get_model('core', 'PostsModel')
    for post in PostsModel.objects.all():
        # Генерируем уникальный slug, например, добавляя id
        post.slug = f"{slugify(post.title)}-{post.id}" 
        post.save()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_postsmodel_slug'), # укажите вашу предыдущую миграцию
    ]
    operations = [
        migrations.RunPython(populate_slugs),
    ]