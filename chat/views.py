from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Mensajes
# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1>Angel Matias Calderón</h1><br/><a href='mensajes'><h2>Mensajes</h2></a>")

def mensajes(request):
    mensaje = Mensajes.objects.all()
    return render(request, 'mensajes.html', {'mensajes': mensaje})