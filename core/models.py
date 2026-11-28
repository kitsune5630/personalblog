from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from transliterate import translit
# put there for auto html generation plus db generation

class TagsModel(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class PostsModel(models.Model):
    """
    Модель профиля пользователя
    params:
    title - заголовок
    slug - кастом пусть (profile/<custom>/)
    text - текст поста
    created_at - когда создано (автодобавление - сейчас)
    author - (ФК)
    """
    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(default=None, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(TagsModel, related_name="posts", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            latin_title = translit(self.title, language_code="ru", reversed=True)
            base_slug = slugify(latin_title)

            slug = base_slug
            counter = 1
            while PostsModel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        try:
            author_name = self.author.username if self.author else "Anon"
        except User.DoesNotExist:
            author_name = "Anon (deleted)"
        title = self.title if self.title else "Unknown"
        return f'Пост {self.id} от {author_name}'

class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, null=True, related_name="comments")
    text = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            author_name = self.author.username if self.author else "Anon"
        except User.DoesNotExist:
            author_name = "Anon (deleted)"
        post_title = self.post.title if self.post else "Unknown"
        return f"Комментарий от {author_name} к посту {post_title}"

class ProfileModel(models.Model):
    """
    Модель профиля пользователя
    params:
    user - пользователь (1к1)
    slug - кастом пусть (profile/<custom>/)
    phone_number - телефон
    telegram - тг
    about_self - о себе
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="Профиль")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=20, blank=True, null=True)
    about_self = models.CharField(max_length=100, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            latin_title = translit(self.user.username, language_code="ru", reversed=True)
            base_slug = slugify(latin_title)

            slug = base_slug
            counter = 1
            while ProfileModel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            # self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        try:
            author_name = self.user.username if self.user else "Anon"
        except User.DoesNotExist:
            author_name = "Anon (deleted)"
        return f'Профиль {author_name}, id = {self.user.id}'

# автосоздание пустого профиля
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)

# class CustomUserModel(AbstractUser):
#     slug = models.SlugField(max_length=100, unique=True, blank=True)
#     phone_number = models.SlugField(max_length=20, blank=True, null=True)

#     def __str__(self):
#         return self.username

# <p><a href="{{ request.META.HTTP_REFERER|default:'/'}}">Назад</a></p>