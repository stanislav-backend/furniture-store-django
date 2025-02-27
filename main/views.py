from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"title": "Home - Главная", "content": "Магазин мебели HOME"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Просто рандом текст",
    }
    return render(request, "main/about.html", context)
