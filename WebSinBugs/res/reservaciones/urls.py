from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('user/login', views.login, name='login'),
    path('user/validate_login', views.validate_login, name='login'),
    path('user/logout', views.logout, name='logout'),
    path('user/registrar', views.registrar, name='user'),
    path('user/ok', views.ok, name='user'),
    path('user/crear_direccion', views.crear_direccion, name='user'),
    path('user/lista_locales', views.lista_locales, name='user'),
]
