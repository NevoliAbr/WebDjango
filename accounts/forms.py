from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    fecha_inicio_trabajo = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Moto
        fields = [
            'modelo',
            'propietario',
            'descripcion',
            'asignado',
            'fecha_inicio_trabajo',
            'precio_mano_obra',
            'precio_accesorios',
            'pago_inicial',
            'imagen',
            'activo',
        ]
        widgets = {
            'modelo': forms.TextInput(),
            'propietario': forms.TextInput(),
            'asignado': forms.TextInput(),
        }
