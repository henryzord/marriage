from bakery.views import BuildableTemplateView
from django.conf import settings
import json
import os
from django.views.generic import TemplateView


class IndexView(BuildableTemplateView):
    template_name = "casamento/index.html"
    build_path = 'index.html'


class PlaceView(BuildableTemplateView):
    template_name = 'casamento/local.html'
    build_path = 'local.html'


class AttendanceView(BuildableTemplateView):
    template_name = 'casamento/presenca.html'
    build_path = 'presenca.html'


class PhotosView(BuildableTemplateView):
    template_name = 'casamento/fotos.html'
    build_path = 'fotos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pics = [x for x in os.listdir(os.path.join(settings.STATICFILES_DIRS[0], 'img', 'gallery')) if '.webp' in x]

        context['photos'] = [
            {'name': f"/marriage/static/img/gallery/{x}", 'number': i}
            for i, x in enumerate(pics)
        ]

        return context


class GiftsView(BuildableTemplateView):
    template_name = 'casamento/presentes.html'
    build_path = 'presentes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(
                os.path.join(str(settings.STATICFILES_DIRS[0]), 'img', 'gifts', 'gifts.json'), 'r', encoding='utf-8'
        ) as gift_file:
            gift_list = json.load(gift_file)
            for item in gift_list:
                item['imagem'] = item['imagem'].replace('{{ STATIC_URL }}', settings.STATIC_URL)

        context['gifts'] = gift_list

        return context
