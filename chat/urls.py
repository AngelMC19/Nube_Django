from django.urls import path
from . import views

urlpatterns = [
    path('',views.bienvenida),
    path('mensajes',views.mensajes)
]