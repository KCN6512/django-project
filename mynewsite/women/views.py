from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
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

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Ошибка при добавлении поста')
    else:
        form = AddPostForm()
    return render(request,'women/addpage.html',{'form':form,'title':'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def addpage(request):
    return HttpResponse('Добавление статьи')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request,post_id): #post_slug
    post = get_object_or_404(Women, pk=post_id) #slug=post_slug

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request,'women/post.html',context=context)