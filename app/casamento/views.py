from bakery.views import BuildableTemplateView
from django.conf import settings
import json
import os
import pathlib


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

    def __recursively_add_pictures__(self, path):
        contents = sorted(os.listdir(path))
        pics = []
        for content in contents:
            rel_path = os.path.join(path, content)
            if os.path.isdir(rel_path):
                pics += self.__recursively_add_pictures__(rel_path)
            elif '.webp' in content.lower():
                pics += ['/'.join([os.path.basename(os.path.dirname(rel_path)), content])]

        return pics

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parent_folder = os.path.join(settings.STATICFILES_DIRS[0], 'img', 'gallery')
        pics = self.__recursively_add_pictures__(parent_folder)

        context['photos'] = [
            {'name': f"{settings.STATIC_URL}img/gallery/{x}", 'number': i}
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
