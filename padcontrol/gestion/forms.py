from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput, forms

from gestion.models import Oficios, Dependencias, Analistas


class Oficioform(ModelForm):
    TIPO_OFICIO = [
        ('REPORTE_PAD', 'REPORTE PAD'),
        ('CONTRATOS', 'CONTRATOS'),
        ('ACTAS_EVALUACION', 'ACTAS DE EVALUACION')
    ]

    class Meta:
        model = Oficios
        fields = '__all__'

        widgets = {
            'n_oficio': TextInput(attrs={'type': 'text', 'required': True}),
            'descripcion': TextInput(attrs={'type': 'text'}),
            'clave_depe': Select(attrs={'autofocus': 'autofocus', 'required': False}),
            'n_pads': NumberInput(attrs={'type': 'number', 'required': True}),
            # 'fecha': DateInput(attrs={'type': 'date', 'required': False}),
            'alcance': Select(attrs={'autofocus': 'autofocus', 'required': False, 'title': 'En alcance de...'}),
            'pendientes': NumberInput(attrs={'type': 'number'}),
            'sustituciones': NumberInput(attrs={'type': 'number'}),
            'altas': NumberInput(attrs={'type': 'number'}),
            'bajas': NumberInput(attrs={'type': 'number'})
        }

    # def __init__(self, *args, **kwargs):
    #   super(Oficioform, self).__init__(*args, **kwargs)
    #  for field in iter(self.fields):
    #     self.fields[field].widget.attrs.update({'class': 'form-control'})
    #  self.fields['alcance'].widget.attrs.update({'autofocus': 'autofocus', 'title': "En alcance de..."})


class Depeform(ModelForm):
    class Meta:
        model = Dependencias
        fields = '__all__'
        widget = {
            'clave': NumberInput(attrs={'type': 'number', 'required': True}),
            'nombre': TextInput(attrs={'type': 'text', 'required': True}),
            'id_analista': Select(attrs={'autofocus': 'autofocus', 'required': True}),
            'inicio_ciclo': DateInput(attrs={'type': 'text', 'required': False}),
            'fin_ciclo': DateInput(attrs={'type': 'text', 'required': False}),
            'n_docentes': NumberInput(attrs={'type': 'number', 'required': False})

        }


class Anaform(ModelForm):
    class Meta:
        model = Analistas
        fields = '__all__'
        widget = {
            'nombre': TextInput(attrs={'type': 'text', 'required': True})
        }
