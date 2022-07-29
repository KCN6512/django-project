from django import template
from women.models import *

register = template.Library() #создание экземпляра класса билблиотеки через который будет происходить регистрация тэгов

@register.simple_tag(name='getcats')#декоратор регистарции | простой тэг
def get_categories():#теперь тэг
    return Category.objects.all()

