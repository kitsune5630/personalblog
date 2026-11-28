from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import CustomAuthenticationForm, PostCreationForm, CustomUserCreationform, ProfileCreationForm, CommentForm
from .models import PostsModel, ProfileModel
from pathlib import Path
import json

# Create your views here.
def home(request):
    """
    Поведение при запроса начальной (главной) страницы
    На данный момент заглушка (пустая)
    """
    context = {
        "count_users": User.objects.count(),
        "count_posts": PostsModel.objects.count(),
    }
    return render(request, "home.html", context=context)

def profile_edit(request):
    """
    Создание профиля пользователя
    """
    # if hasattr(request.user, 'profile'):
    #     return redirect('home')
    profile = request.user.profile
    if request.method == "POST":
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            # если models.ModelForm
            # profile = profile_form.save(commit=False)
            # profile.user = request.user
            # profile.save()
            profile.phone_number = profile_form.cleaned_data["phone_number"].strip()
            profile.telegram = profile_form.cleaned_data["telegram"].strip()
            profile.about_self = profile_form.cleaned_data["about_self"].strip()
            profile.save()
            return redirect("profile_user", slug=profile.slug)
    else:
        initial_data = {
            'phone_number': profile.phone_number,
            'telegram': profile.telegram,
            'about_self': profile.about_self,
        }
        profile_form = ProfileCreationForm(initial=initial_data)
    return render(request, "profile_create.html", {"profile_form": profile_form})

def profile_user(request, slug):
    """
    Профиль пользователя
    """
    profile = get_object_or_404(ProfileModel, slug=slug)
    user = profile.user
    posts = PostsModel.objects.filter(author_id=user.id)
    context = {
        "user": user, "profile": profile, "posts": posts
    }
    return render(request, "profile_user.html", context=context)

def posts(request):
    """
    Страница со всеми имеющимися постами
    """
    posts_list = PostsModel.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { "posts": page_obj }
    return render(request, "posts.html", context=context)

def post_detail(request, slug):
    """
    Детали поста
    """
    post = get_object_or_404(PostsModel, slug=slug)
    comments = post.comments.all().order_by('created_at')
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", slug=slug)
    else:
        comment_form = CommentForm()
    context = {
        "post": post, "comments": comments, "comment_form":comment_form
    }
    return render(request, "post_detail.html", context=context)

    #return render(request, "post_detail.html", {"post": post})

def post_edit(request, slug):
    """
    Редактирование поста
    """
    post = get_object_or_404(PostsModel, slug=slug)
    if request.method == "POST":
        post_editform = PostCreationForm(request.POST)
        if post_editform.is_valid():
            post.title = post_editform.cleaned_data["title"].strip()
            post.text = post_editform.cleaned_data["text"].strip()
            post.save()
            return redirect("post_detail", slug=slug)
    else:
        initial_data = {
            'title': post.title,
            'text': post.text,
        }
        post_editform = PostCreationForm(initial=initial_data)
    return render(request, "post_edit.html", {"post_editform": post_editform})

def post_create(request):
    """
    Создание поста
    """
    if request.method == "POST":
        post_createform = PostCreationForm(request.POST)
        if post_createform.is_valid():
            title = post_createform.cleaned_data["title"].strip()
            text = post_createform.cleaned_data["text"].strip()
            author = request.user
            PostsModel.objects.create(
                title=title, text=text, author=author
            )
            messages.success(request, "Пост успешно создан!")
            return redirect("success_post_create")
    else:
        post_createform = PostCreationForm()
    context = {"form": post_createform }
    return render(request, "post_create.html", context=context)

def success_post_create(request):
    """
    Успешное создание поста
    """
    return render(request, "success_post_create.html")

def registration(request):
    """
    Поведение при запросе страницы "Регистрация"
    добавлена таблица для юзера с уникальными полями
    """
    if request.method == "POST":
        user_registrationform = CustomUserCreationform(request.POST)
        if user_registrationform.is_valid():
            user = user_registrationform.save()
            login(request, user)
            return redirect("profile_edit")
    else:
        user_registrationform = CustomUserCreationform()
    context = {"form": user_registrationform}
    return render(request, "registration.html", context=context)

def login_view(request):
    form = CustomAuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"].strip()
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("success_login")
    return render(request, "registration/login.html", {'form': form})


# class MyLoginView(LoginView):
    """
    Кастом логин вьюха
    """
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm 

def success_login(request):
    """
    Вывод страницы при успешном входе
    """
    return render(request, "success_login.html")

def about(request):
    """
    Поведение запроса страницы "Информация" / "Обо мне" (название пока первое)
    """
    with open((Path(__file__).parent) / 'static/json/about.json', 'r', encoding="UTF-8") as f:
        context = json.load(f)
    return render(request, "about.html", context=context)
