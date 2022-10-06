from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('llantas', views.llantas, name='llantas'),
    path('llantas/crear', views.crear_llanta, name='crear_llanta'),
    path('llantas/editar', views.editar_llanta, name='editar_llanta'),
    path('llantas/borrar/<int:id>', views.borrar_llanta, name='borrar_llanta'),
    path('llantas/editar/<int:id>', views.editar_llanta, name='editar_llanta'),
]