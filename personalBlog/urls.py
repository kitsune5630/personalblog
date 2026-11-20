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

urlpatterns = [
    path("", views.home, name='home'),
    path("references/", views.references, name='references'),
    path("about/", views.about, name='about'),
    path("login/", views.login, name='login'),
    path("login/success/", views.success_login, name='success_login'),
    path("registration/", views.registration, name="registration"),
    path("registration/success/", views.success_registration, name='success_registration'),
    path("post/1/", views.post_detail, name="post_detail"),
    
]
