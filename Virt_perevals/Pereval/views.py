from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import UserSerializer, CoordinateSerializer, LevelSerializer, PerevalSerializer, ImageSerializer, \
    PerevalListSerializer


class UserViewset(viewsets.ModelViewSet):

    queryset = PerevalUser.objects.all()
    serializer_class = UserSerializer


class CoordinateViewset(viewsets.ModelViewSet):

    queryset = PerevalCoordinate.objects.all()
    serializer_class = CoordinateSerializer


class LevelViewset(viewsets.ModelViewSet):

    queryset = PerevalLevel.objects.all()
    serializer_class = LevelSerializer


class ImageViewset(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PerevalViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.filter(id=0)
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        response_data = {}

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 200,
                'message': '',
                'id': serializer.data.get('id')
            }

        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            response_data = {
                'status': 500,
                'message': 'Ошибка подключения к базе данных',
                'id': serializer.data.get('id')
            }

        elif status.HTTP_400_BAD_REQUEST:
            response_data = {
                'status': 400,
                'message': 'Неверный запрос',
                'id': serializer.data.get('id')
            }

        return Response(response_data)


class PerevalListView(APIView):
