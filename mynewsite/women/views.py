from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Страница приложения women')

def categories(request,catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def mainpage(request):
    return HttpResponse('Главная страница сайта')

def archive(request,year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}<p>')