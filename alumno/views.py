from django.shortcuts import render, redirect
from .models import Alumno
from django.contrib import messages

def home(request):
    alumnosListados = Alumno.objects.all()
    messages.success(request, '¡Alumnos listados!')
    return render(request, "gestionAlumno.html", {"alumnos": alumnosListados})

def registrarAlumno(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']

        alumno = Alumno.objects.create(
            codigo=codigo, nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
        messages.success(request, '¡Alumno registrado!')
        return redirect('/')

def edicionAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    return render(request, "edicionAlumno.html", {"alumno": alumno})

def editarAlumno(request):
    if request.method == 'POST':
        id = request.POST['id']
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']

        alumno = Alumno.objects.get(id=id)
        alumno.codigo = codigo
        alumno.nombre = nombre
        alumno.edad = edad
        alumno.direccion = direccion
        alumno.telefono = telefono
        alumno.save()

        messages.success(request, '¡Alumno actualizado!')

        return redirect('/')

    return render(request, "edicionAlumno.html")  # Debes crear una página HTML para el formulario de edición de alumnos

def eliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    messages.success(request, '¡Alumno eliminado!')

    return redirect('/')
