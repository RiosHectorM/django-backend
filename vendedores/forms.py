from django.forms import ModelForm
from .models import Vendedores


class VendedorForm(ModelForm):
    class Meta:
        model = Vendedores
        fields = ['nombre', 'apellido', 'email',
                  'empresa', 'direccion', 'telefono']
