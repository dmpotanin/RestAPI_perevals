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

    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


class PerevalListView(APIView):

    def get(self, request):

        perevals = PerevalAdded.objects.all()
        serializer = PerevalListSerializer(perevals, many=True)

        return Response(serializer.data)