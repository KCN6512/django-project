from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    #prepopulated_fields = {'slug': ('title',)} используется для автосоздания slug'a


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)#нужно передать кортеж поэтому запятая,
    #prepopulated_fields = {'slug': ('name',)} используется для автосоздания slug'a

admin.site.register(Women,WomenAdmin) #регистрация в админ панели модели Women
admin.site.register(Category,CategoryAdmin)