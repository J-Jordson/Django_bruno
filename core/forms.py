from tkinter import Widget
from django import forms
from .models import Curso, Area


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'data_inicio', 'vagas', 'area', 'publico']
        widgets = {
            'area': forms.RadioSelect(),
            'publico': forms.CheckboxSelectMultiple(),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']