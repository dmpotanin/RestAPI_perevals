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

    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    status = serializers.CharField(read_only=True)
    user = UserSerializer()
    coord = CoordinateSerializer()
    level = LevelSerializer(allow_null=True, default=False)

    class Meta:
        model = PerevalAdded
        fields = [
            'id', 'status', 'beauty_title', 'title', 'other_title', 'connect',
            'add_time', 'user', 'coord', 'level', 'images'
        ]

    class PerevalListSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True)
        add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
        user = UserSerializer()
        coord = CoordinateSerializer()
        level = LevelSerializer()

        class Meta:
            model = PerevalAdded
            fields = [
                'id', 'status', 'beauty_title', 'title', 'other_title', 'connect',
                'add_time', 'user', 'coord', 'level', 'images'
            ]