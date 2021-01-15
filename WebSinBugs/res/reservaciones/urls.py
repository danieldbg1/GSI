from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.login, name='user'),
    path('user/login', views.login, name='user'),
    path('user/registrar', views.registrar, name='user'),
    path('user/ok', views.ok, name='user'),
    path('user/crear_direccion', views.crear_direccion, name='user'),
    path('user/lista_locales', views.lista_locales, name='user'),
]