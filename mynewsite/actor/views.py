from typing import Any, Dict
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

class ActorHome(DataMixin,ListView):# self.object_list
    model = Actor
    template_name = 'actor/index.html'
    context_object_name =  'posts'
   
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self): # фильтр queryset
        return Actor.objects.filter(is_published=True).select_related('cat') #предварительанпя загрузка данных из связанрой модели

class ActorCategory(DataMixin,ListView):#self.object_list
    model = Actor
    template_name = 'actor/index.html'
    context_object_name = 'posts'
    allow_empty = False # если страница пустая выдаст 404 

    def get_queryset(self):#получить queryset откуда брать информацию
        return Actor.objects.filter(cat_id=self.kwargs['cat_id'], is_published=True).select_related('cat')#kwargs все параметры запроса

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        catg = Category.objects.get(pk=self.kwargs['cat_id'])
        context['title'] = 'Категория - ' + str(catg.name)
        context['cat_selected'] = catg.pk
        return context

class AddPage(LoginRequiredMixin, CreateView): #вью для форм
    form_class = AddPostForm
    template_name = 'actor/addpage.html'
    #автоматически редирект на get_absolute_url модели
    #telegram send_msg('User добавил статью')
    success_url = reverse_lazy('home')#ручной редирект
    login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context

class AddCategory(LoginRequiredMixin,CreateView):
    form_class = AddCategoryForm
    template_name = 'actor/addcategory.html'
    success_url = reverse_lazy('home')#ручной редирект
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление категории'
        return context

class ShowPost(DetailView): #self.object
    model = Actor
    template_name = 'actor/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post' # без этого получится {% for publisher in object %} с ним {% for publisher in post %}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #для передачи контекста в темплейт
        context =  super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context

class Tablica(ListView):
    model = Actor
    template_name = 'actor/tablica.html'
    context_object_name = 'zapis'

    def get_queryset(self):#получить queryset откуда брать информацию
        return Actor.objects.values('title','cat__name')#kwargs все параметры запроса
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Таблица'
        return context

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'actor/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'actor/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect('login')

class ContactFormView(FormView): # formview не связан с базой данных
    form_class = ContactForm
    template_name = 'actor/contact.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ActorUpdate(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ['title', 'content']
    #template_name = 'actor/actor_update.html' #всегда нужно указывать папку
    template_name_suffix = '_update_form'

    def get_queryset(self) -> models.query.QuerySet:
        return Actor.objects.filter(pk=self.kwargs['post_pk'])

    pk_url_kwarg = 'post_pk' # обязательно для UpdateView

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def not_enough_premission(request, exception):
    return HttpResponseForbidden('<h1>У вас недостаточно прав,пожалуйста зарегистрируйтесь на сайте, или войдите под своим логином</h1>')
