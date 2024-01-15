from django.urls import path
from django_distill import distill_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('local', views.place, name='local do evento'),
    path('fotos', views.photos, name='galeria de fotos'),
    path('presentes', views.gifts, name='lista de presentes'),
    # distill_path('presentes.html', views.gifts, name='lista de presentes'),  # TODO para gerar as páginas, use assim
    path('presenca', views.attendance, name='confirmar presença'),
]