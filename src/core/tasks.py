import time
from celery import shared_task
from .models import File


@shared_task
def upload_file(file_id):
    time.sleep(5)
    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()
