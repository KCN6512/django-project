from django.urls import path

from .views import *
#urlки нужно закрывать слэшэм /
urlpatterns = [
    path('', WomenHome.as_view(), name='home'),# необходимо вызвать как view()
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', ShowPost.as_view(),name='post'), #slug:post_slug
    path('category/<int:cat_id>', WomenCategory.as_view(), name='category'),
]
