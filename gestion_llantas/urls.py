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
    path('actividad_dos', views.actividad_dos, name='actividad_dos'),
    path('actividad_tres', views.actividad_tres, name='actividad_tres'),
    path('punto_dos', views.punto_dos, name='punto_dos'),
    path('punto_tres', views.punto_tres, name='punto_tres'),
]