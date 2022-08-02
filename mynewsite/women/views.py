from typing import Any, Dict
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name =  'posts'  

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self): # фильтр queryset
        return Women.objects.filter(is_published=True)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # если страница пустая выдаст 404 

    def get_queryset(self):
        return Women.objects.filter(cat_id=self.kwargs['cat_id'], is_published=True)#kwargs все параметры запроса

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

def about(request):
    return render(request,'women/about.html',{'title': 'О сайте'})

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    #автоматически редирект на get_absolute_url модели
    success_url = reverse_lazy('home')#ручной редирект

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def contact(request):
    return HttpResponse('Обратная связь')

def addpage(request):
    return HttpResponse('Добавление статьи')

def login(request):
    return HttpResponse('Авторизация')

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    pk_url_kwarg = 'post_id' #или pk или slug используется
    context_object_name = 'post' # без этого получится {% for publisher in object_list %} с ним {% for publisher in post %}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context