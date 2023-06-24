from rest_framework import serializers
from django.core.files.storage import FileSystemStorage
from django.core.files import File as DjangoFile
from .models import File
from .tasks import upload_file
from django.core.files.uploadedfile import SimpleUploadedFile


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file']

    def save(self, **kwargs):
        file = self.context['file']
        file_object = File.objects.create(
            file=SimpleUploadedFile(file.name, '')
        )
        storage = FileSystemStorage()
        storage.save(file.name, DjangoFile(file))
        upload_file.delay(file_id=file_object.id, path=storage.path(file.name), file_name=file.name)
        return file_object


class FileRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file', 'processed', 'uploaded_at']
