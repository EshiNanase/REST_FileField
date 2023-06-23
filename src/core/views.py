from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FileSerializer
from http import HTTPStatus


@api_view(['POST'])
def create_file(request):

    serializer = FileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=HTTPStatus.CREATED)
