from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import llanta
from .forms import LlantaForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def llantas(request):
    llantas = llanta.objects.all()
    return render(request, 'llantas/index.html', {'llantas': llantas})

def crear_llanta(request):
    formulario = LlantaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('llantas')
    return render(request, 'llantas/crear.html', {'formulario': formulario})

def editar_llanta(request, id):
    data = llanta.objects.get(id=id)
    formulario = LlantaForm(request.POST or None, request.FILES or None, instance=data)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('llantas')
    return render(request, 'llantas/editar.html', {'formulario': formulario})

def borrar_llanta(request, id):
    data = llanta.objects.get(id=id)
    data.delete()
    return redirect('llantas')