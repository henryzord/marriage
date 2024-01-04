from django.shortcuts import render
from django.conf import settings
import json
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
        'photos': [{'name': f"/static/images/gallery/{x}", 'number': i} for i, x in
        enumerate(os.listdir(os.path.join(str(settings.STATICFILES_DIRS[0]), 'images', 'gallery')))]
    }
    return render(
        request,
        'casamento/fotos.html',
        context=photos
    )


def gifts(request):
    with open(os.path.join(str(settings.STATICFILES_DIRS[0]), 'images', 'gifts', 'gifts.json'), 'r') as gift_file:
        gifts = json.load(gift_file)

    return render(
        request,
        'casamento/presentes.html',
        context={'gifts': gifts}
    )
