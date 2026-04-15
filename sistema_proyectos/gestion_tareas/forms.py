from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'placeholder': 'Nombre del proyecto'}),
            'descripcion': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'rows': 3, 'placeholder': 'Breve descripción...'}),
        }
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'rows': 2, 'placeholder': 'Detalles de la tarea...'}),
            'completada': forms.CheckboxInput(attrs={'style': 'margin-bottom: 15px;'}),
        }