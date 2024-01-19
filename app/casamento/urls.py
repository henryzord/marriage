from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index', views.IndexView.as_view(), name='index'),
    path('local', views.PlaceView.as_view(), name='local do evento'),
    # path('fotos', views.photos, name='galeria de fotos'),
    path('fotos', views.PhotosView.as_view(), name='galeria de fotos'),
    path('presentes', views.GiftsView.as_view(), name='lista de presentes'),
    path('presenca', views.AttendanceView.as_view(), name='confirmar presença'),
]
