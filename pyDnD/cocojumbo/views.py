from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("We gotta do something about this. I do not know Django yet!!!")

def login(request):
    return HttpResponse("Here we're gonna make a login page :*")