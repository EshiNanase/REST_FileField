from rest_framework import serializers
from django.core.files.storage import FileSystemStorage
from django.core.files import File as DjangoFile
from .models import File
from .tasks import upload_file


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file']

    def save(self, **kwargs):
        file_object = File.objects.create()
        file = self.context['file']
        storage = FileSystemStorage()
        storage.save(file.name, DjangoFile(file))
        upload_file.delay(file_id=file_object.id, path=storage.path(file.name), file_name=file.name)
        return file_object

