from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/login', views.login, name='user'),
    path('user/registrar', views.registrar, name='user'),
    path('user/ok', views.ok, name='user'),
    #path('user/fallo_registrar', views.ok, name='user'),
]