from re import M
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *


menu = [
    {'title': "О сайте",'url_name':'about'},
    {'title': "Добавить статью",'url_name':'add_page'},
    {'title': "Обратная связь",'url_name':'contact'},
    {'title': "Войти",'url_name':'login'},
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats' : cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request,'women/index.html',context=context)

def about(request):
    return render(request,'women/about.html',{'title': 'О сайте','menu': menu})


def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def addpage(request):
    return HttpResponse('Добавление статьи')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request,post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def show_category(request,cat_id):
    return HttpResponse(f'Отображение категории с id = {cat_id}')