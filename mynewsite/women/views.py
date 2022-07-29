from re import M
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *





def index(request):
    posts = Women.objects.filter(is_published=True)
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request,'women/index.html',context=context)
    
def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if not posts:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request,'women/index.html',context=context)

def about(request):
    return render(request,'women/about.html',{'title': 'О сайте'})

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
