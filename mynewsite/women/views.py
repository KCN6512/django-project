from typing import Any, Dict
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import *

class WomenHome(DataMixin,ListView):# self.object_list
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

class WomenCategory(DataMixin,ListView):#self.object_list
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # если страница пустая выдаст 404 

    def get_queryset(self):#получить queryset откуда брать информацию
        return Women.objects.filter(cat_id=self.kwargs['cat_id'], is_published=True)#kwargs все параметры запроса

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

class AddPage(LoginRequiredMixin, CreateView): #вью для форм
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    #автоматически редирект на get_absolute_url модели
    #telegram send_msg('User добавил статью')
    success_url = reverse_lazy('home')#ручной редирект
    login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context

class ShowPost(DetailView): #self.object
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post' # без этого получится {% for publisher in object %} с ним {% for publisher in post %}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context

class Tablica(ListView):
    model = Women
    template_name = 'women/tablica.html'
    context_object_name = 'zapis'

    def get_queryset(self):#получить queryset откуда брать информацию
        return Women.objects.values('title','cat__name')#kwargs все параметры запроса
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Таблица'
        return context

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def about(request):
    return render(request,'women/about.html',{'title': 'О сайте'})

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
