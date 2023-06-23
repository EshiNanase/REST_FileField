from django.urls import path
from .views import create_file


urlpatterns = [
    path('upload/', create_file),
]
