from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import staticfiles
from django.conf import settings
import os


def index(request):
    return render(
        request,
        'casamento/index.html'
    )


def place(request):
    return render(
        request,
        'casamento/local.html'
    )


# TODO nota para o futuro: servir arquivos estáticos assim não
#  é eficiente. Ler a documentação do DJango para mais detalhes!
def photos(request):
    photos = {
        'photos': [f"/static/images/gallery/{x}" for x in
        os.listdir(os.path.join(str(settings.STATICFILES_DIRS[0]), 'images', 'gallery'))]
    }
    return render(
        request,
        'casamento/fotos.html',
        context=photos
    )
