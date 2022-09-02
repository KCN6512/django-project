from django import template
from actor.models import *

register = template.Library() #создание экземпляра класса билблиотеки через который будет происходить регистрация тэгов

@register.simple_tag(name='getcats')#декоратор регистарции | простой тэг
def get_categories(filter=None):#теперь тэг
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag(filename='actor/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else: 
        cats = Category.objects.order_by(sort)

    return {'cats':cats,'cat_selected':cat_selected}

@register.inclusion_tag(filename='actor/list_menu.html',takes_context=True)
def show_menu(context):
    menu = [
    {'title': "Добавить статью",'url_name':'add_page'},
    {'title': "Добавить категорию",'url_name':'add_category'},
    {'title': "Таблица",'url_name':'tablica'},
    
]
    context['menu'] = menu
    return context