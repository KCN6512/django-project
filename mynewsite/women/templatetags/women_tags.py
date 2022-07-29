from django import template
from women.models import *

register = template.Library() #создание экземпляра класса билблиотеки через который будет происходить регистрация тэгов

@register.simple_tag(name='getcats')#декоратор регистарции | простой тэг
def get_categories(filter=None):#теперь тэг
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag(filename='women/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else: 
        cats = Category.objects.order_by(sort)

    return {'cats':cats,'cat_selected':cat_selected}