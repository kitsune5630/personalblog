"""
URL configuration for personalBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

admin.site.has_permission = lambda request: request.user.is_active and request.user.is_superuser

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", views.home, name='home'),

    # логин + успех
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("login/success/", views.success_login, name='success_login'),

    # регистрация
    path("signup/", views.registration, name="registration"),

    # страница с постами + сам пост + создание поста
    path("posts/", views.posts, name='posts'),
    path("post/create/", views.post_create, name="post_create"),
    path("post/success_post_create/", views.success_post_create, name="success_post_create"),
    path("post/edit/<slug:slug>/", views.post_edit, name="post_edit"),
    # # комменты - привязано к посту, под постом
    # path("post/<slug:slug>/comment/", views.post_comment, name="post_comment"), 
    # путь к посту с именем (заголовок поста, пока онли англ. -> переделать на все языки)
    # path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),

    # профиль пользователя
    # path("profile/<int:pk>/", views.profile_user, name="profile_user"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("profile/<slug:slug>/", views.profile_user, name="profile_user"),

    # поиск
    path("search/", views.search, name="post_search"),

    # обо мне
    path("about/", views.about, name='about'),
]
