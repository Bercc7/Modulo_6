from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

@login_required
def home(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)

    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            nuevo_proyecto = form.save(commit=False)
            nuevo_proyecto.usuario = request.user 
            nuevo_proyecto.save()
            return redirect('home') 
    else:
        form = ProyectoForm()

    return render(request, 'home.html', {
        'proyectos': proyectos,
        'form': form
    })
@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=request.user)
    
    tareas = Tarea.objects.filter(proyecto=proyecto)

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)
            nueva_tarea.proyecto = proyecto
            nueva_tarea.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = TareaForm()

    return render(request, 'detalle_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas,
        'form': form
    })