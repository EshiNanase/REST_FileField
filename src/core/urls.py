from django.urls import path
from .views import create_file, get_files


urlpatterns = [
    path('upload/', create_file),
    path('files/', get_files),
]
