from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('local', views.place, name='local do evento'),
    path('fotos', views.photos, name='galeria de fotos'),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# TODO nota para o futuro: servir arquivos estáticos assim não
#  é eficiente. Ler a documentação do DJango para mais detalhes!
