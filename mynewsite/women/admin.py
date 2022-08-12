from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','is_published') # gethtmlphoto тобразить фотографии
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    #prepopulated_fields = {'slug': ('title',)} используется для автосоздания slug'a
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')# поля выводимые в админку при редактировании | только после readonly_fields можно жсюда добавить 'time_create', 'time_update'
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')#нередактируемые поля

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>') #marksafe не экранирует тэги html
    
    get_html_photo.short_description = 'Мини фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)#нужно передать кортеж поэтому запятая,

admin.site.register(Women,WomenAdmin) #регистрация в админ панели модели Women
admin.site.register(Category,CategoryAdmin)