from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Main")


def cats(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Cat: </h1> <p>{cat}</p>")


def archive(request, year):
    if year > 2100:
        raise redirect("home", permanent=True) #можно использовать для page not found: Http404
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
