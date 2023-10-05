from django.forms import ModelForm
from .models import Curso, Area


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'data_inicio', 'vagas', 'area', 'publico']

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']