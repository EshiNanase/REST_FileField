from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .serializers import FileSerializer
from .models import File
from http import HTTPStatus


@extend_schema(request=FileSerializer)
@api_view(['POST'])
def create_file(request):

    file = request.FILES['file']

    serializer = FileSerializer(
        data=request.data,
        context={
            'file': file
        }
    )
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            data={'file': file.name},
            status=HTTPStatus.CREATED
        )
    else:
        return Response(
            data=serializer.errors,
            status=HTTPStatus.BAD_REQUEST
        )


@api_view(['GET'])
def get_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(
        data=serializer.data,
        status=HTTPStatus.OK
    )
