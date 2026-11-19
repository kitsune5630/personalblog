from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .forms import UserForm

# Create your views here.
def home(request):

    return render(request, "home.html")

def login(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            # username = userform.cleaned_data["username"]
            # password = userform.cleaned_data["password"]
            messages.success(request, "Вы успешно авторизованы!")
            return redirect("success_login")
    else:
        userform = UserForm()
    context = {"form": userform}
    return render(request, "login.html", context=context)

def success_login(request):
    return render(request, "success_login.html")

def references(request):
    github_ref = "https://github.com/kitsune5630"
    leetcode_ref = "https://leetcode.com/u/kitsune12345/"
    data = {
        'github_ref' : github_ref,
        'leetcode_ref' : leetcode_ref,
    }
    return render(request, "references.html", context=data)

def about(request):
    context = {
        "personalphoto": "/static/images/personalphoto.png", 
        "name": "Иван", "lastname": "Иванов", "surname": "Иванович",
        "skills": [
            "Python", "Django", "HTML/CSS", 
            "GIT", "DOCKER", "REST API"
        ],
        "projects": [
            {"title": "Блог", "url": "https://github.com/kitsune5630/personalblog"},
        ],
        "education": {
            "image": "/static/images/Nstu.jpg", 
            "name": "Новосибирский Государственный Технический Университет",
            "shortname": "НГТУ",
            "speciality": "Программное обеспечение компьютерных систем и сетей",
            "course": "4",
        },
        "contact_info": {
            "telegram": "@kitsune5630",
            "telegram_url": "https://t.me/kitsune5630",
            "mail": "kitsune5630@proton.me"
        }
    }
    return render(request, "about.html", context=context)

