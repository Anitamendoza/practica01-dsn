from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarAlumno/', views.registrarAlumno),
    path('edicionAlumno/<codigo>', views.edicionAlumno),
    path('editarAlumno/', views.editarAlumno),
    path('eliminarAlumno/<codigo>', views.eliminarAlumno)
]
