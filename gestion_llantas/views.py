from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import llanta
from .forms import LlantaForm
# Create your views here.

def inicio(request):
    llantas = llanta.objects.all()
    return render(request, 'llantas/index.html', {'llantas': llantas})

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

def actividad_dos(request):
    return render(request, 'actividad_dos/actividad_dos.html')

def actividad_tres(request):
    return render(request, 'actividad_tres/actividad_tres.html')

def punto_dos(request):
    resultado=''
    punto = request.POST.get('punto')
    if punto=='1':
        nombre = request.POST.get('nombre')
        resultado = "Hola " + nombre
    if punto=='2':
        primero_numero = int(request.POST.get('primer_numero'))
        segundo_numero = int(request.POST.get('segundo_numero'))
        resultado = primero_numero*segundo_numero
    return render(request, 'actividad_dos/resultado.html', {'resultado': resultado,'punto':punto})

def punto_tres(request):
    return render(request, 'actividad_tres/resultado.html', {'resultado': resultado,'punto':punto})