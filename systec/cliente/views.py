from django.shortcuts import render


def registrar(request):
    titulo = 'Registrar Cliente'
    context = {
        'titulo' : titulo
    }
    return render(request, 'base.html', context)