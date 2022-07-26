from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',) #нужно передать кортеж поэтому запятая,

class CategoriesInline(admin.TabularInline):
    model = Actor.cat.through
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','is_published') # gethtmlphoto тобразить фотографии
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    #prepopulated_fields = {'slug': ('title',)} используется для автосоздания slug'a
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update', 'likes')# поля выводимые в админку при редактировании | только после readonly_fields можно жсюда добавить 'time_create', 'time_update'
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'slug', 'likes')#нередактируемые поля
    inlines = [CategoriesInline] #удобный выбор категория inline

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>') #marksafe не экранирует тэги html
    
    get_html_photo.short_description = 'Мини фото'



admin.site.register(Actor,ActorAdmin) #регистрация в админ панели модели Actor
admin.site.register(Category,CategoryAdmin)