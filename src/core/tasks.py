from celery import shared_task
from .models import File
from django.core.files import File as DjangoFile
from django.core.files.storage import FileSystemStorage
from pathlib import Path


@shared_task
def upload_file(file_id, path, file_name):

    storage = FileSystemStorage()

    path_object = Path(path)
    instance = File.objects.get(id=file_id)

    with path_object.open(mode='rb') as file:
        django_file = DjangoFile(file, name=path_object.name)
        instance.file = django_file
        instance.processed = True
        instance.save()

    storage.delete(file_name)
