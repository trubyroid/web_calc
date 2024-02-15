from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("Главная страница")


def tmp(request, id):
    return HttpResponse(f"<h1>Id - {id}</h1>")


def re_tmp(request, year):
    return HttpResponse(f"<h1>Year - {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Sorry, page not found")
