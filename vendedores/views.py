from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import VendedorForm
from .models import Vendedores

# Create your views here.


def vendedores(request):
    vendedores = Vendedores.objects.all()
    return render(request, 'vendedores.html', {'vendedores': vendedores})


def create_vendedor(request):
    if request.method == 'GET':
        return render(request, 'create_vendedor.html', {
            'form': VendedorForm
        })
    else:
        try:
            form = VendedorForm(request.POST)
            new_vendedor = form.save(commit=False)
            new_vendedor.user = request.user
            new_vendedor.save()
            return redirect('vendedores')
        except ValueError:
            return render(request, 'create_vendedor.html', {
                'form': VendedorForm,
                'error': 'Ingrese datos validos'
            })


def detail_vendedor(request, vendedor_id):
    return render(request, 'create_vendedor.html')
