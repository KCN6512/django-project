from django.urls import include, path
from .views import *


#urlки нужно закрывать слэшэм /
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', ActorHome.as_view(), name='home'),# необходимо вызвать как view()
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(),name='post'), #slug:post_slug int:pk для Detail view
    path('category/<int:cat_id>', ActorCategory.as_view(), name='category'),
    path('tablica/', Tablica.as_view(), name='tablica'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('actor_update/<int:post_pk>', ActorUpdate.as_view(), name='actor_update'),
    path('actor_delete/<slug:slug>', ActorDelete.as_view(), name='actor_delete'),
]
