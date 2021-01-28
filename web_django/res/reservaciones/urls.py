from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/login', views.login, name='login'),
    path('user/validate_login', views.validate_login, name='login'),
    path('user/logout', views.logout, name='logout'),
    path('user/registrar', views.registrar, name='user'),
    path('user/ok', views.ok, name='user'),
    path('user/crear_direccion', views.crear_direccion, name='user'),
    path('user/lista_locales', views.lista_locales, name='user'),
    path('user/reservar', views.reservar, name='user'),
    path('user/ok_reserva', views.ok_reserva, name='user'),
    path('user/mal_reserva', views.mal_reserva, name='user'),
    path('user/ok_review', views.ok_review, name='user'),
    path('user/mal_review', views.mal_review, name='user'),
    path('user/review', views.review, name='user'),
]
