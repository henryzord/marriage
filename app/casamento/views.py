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


def attendance(request):
    return render(
        request,
        'casamento/presenca.html'
    )


# TODO nota para o futuro: servir arquivos estáticos assim não
#  é eficiente. Ler a documentação do DJango para mais detalhes!
def photos(request):
    photo_list = {
        'photos': [{'name': f"/static/images/gallery/{x}", 'number': i} for i, x in
        enumerate(os.listdir(os.path.join(str(settings.STATICFILES_DIRS[0]), 'images', 'gallery')))]
    }
    return render(
        request,
        'casamento/fotos.html',
        context=photo_list
    )


def gifts(request):
    with open(
        os.path.join(str(settings.STATICFILES_DIRS[0]), 'images', 'gifts', 'gifts.json'), 'r', encoding='utf-8'
    ) as gift_file:
        gift_list = json.load(gift_file)

    context = {'gifts': gift_list}

    return render(
        request,
        'casamento/presentes.html',
        context=context
    )
