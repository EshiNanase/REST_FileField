from celery import shared_task
from django.core.files import File as DjangoFile
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from .models import File


@shared_task
def upload_file(file_object):
    storage = FileSystemStorage()

    path_object = Path(f'media')

    with path_object.open(mode='rb') as file:
        django_file = DjangoFile(file, name=path_object.name)
        django_file.
        instance = ProductImage(product_id=product_id, image=picture)

        instance.save()

    storage.delete(file_name)
