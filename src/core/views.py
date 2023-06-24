from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FileSerializer
from .tasks import upload_file
from .models import File
from http import HTTPStatus


@api_view(['POST'])
def create_file(request):

    serializer = FileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.save()
    upload_file.delay(file.id)
    return Response(
        data=serializer.data,
        status=HTTPStatus.CREATED
    )


@api_view(['GET'])
def get_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(
        data=serializer.data,
        status=HTTPStatus.OK
    )
