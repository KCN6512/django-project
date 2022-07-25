from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render


def categories(request,catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def mainpage(request):
    return render(request,'')

def women_mainpage(request):
    return HttpResponse('Главная страница раздела women')

def archive(request,year):
    if int(year) > 2022:
        return redirect('women-home')
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}<p>')

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
