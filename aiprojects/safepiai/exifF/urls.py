from django.urls import path
from .views import remove_exif
from . import views

urlpatterns=[
    path('remove-exif/', views.remove_exif, name='remove_exif'),
]