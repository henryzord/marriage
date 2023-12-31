from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('marriage/', include('marriage.urls')),
    path('admin/', admin.site.urls),
]