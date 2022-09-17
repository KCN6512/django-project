from django.urls import include, path

from .views import *

#urlки нужно закрывать слэшэм /
urlpatterns = [
    path('', ActorHome.as_view(), name='home'),# необходимо вызвать как view()
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(),name='post'), #slug:post_slug int:pk для Detail view
    path('category/<int:cat_id>', ActorCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('actor_update/<int:post_pk>', ActorUpdate.as_view(), name='actor_update'),
    path('actor_delete/<slug:slug>', ActorDelete.as_view(), name='actor_delete'),
    path('like/<slug:slug>', like_view, name='like_post'),
]
