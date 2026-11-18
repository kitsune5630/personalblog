from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def home(request):
    return render(request, "home.html")

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
        "name": "Иван", "lastname": "Иванов", "surname": "Иванович",
        "skills": ["Python", "Django", "HTML/CSS", "GIT", "DOCKER", "REST API"],
        "projects": [
            {"title": "Блог", "url": "https://github.com/kitsune5630/personalblog"},
        ],
        "education": {
            "image": "...", 
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

