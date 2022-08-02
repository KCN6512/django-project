from django.urls import path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),# необходимо вызвать как view()
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', show_post,name='post'), #slug:post_slug
    path('category/<int:cat_id>', show_category, name='category'),
]
