from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalUser
        fields = ['email', 'surname', 'name', 'otc', 'phone',]


class CoordinateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalCoordinate
        fields = ['latitude', 'longitude', 'height',]


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalLevel
        fields = ['winter', 'summer', 'autumn', 'spring',]


class ImageSerializer(serializers.ModelSerializer):

    data = serializers.URLField()

    class Meta:
        model = Image
        fields = ['title', 'data',]


class PerevalSerializer(WritableNestedModelSerializer):

    user = UserSerializer()
    coord = CoordinateSerializer()
    level = LevelSerializer(allow_null=True, default=False)
    images = ImageSerializer(many=True)

    class Meta:

        model = PerevalAdded
        fields = [
            'id', 'beauty_title', 'title', 'other_title', 'connect',
            'add_time', 'user', 'coord', 'level', 'images'
        ]