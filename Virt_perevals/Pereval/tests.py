from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import PerevalSerializer
from .models import *


class PerevalTestCase(APITestCase):

    def setUp(self):
        # Объект перевал 1
        self.pereval_1 = PerevalAdded.objects.create(
            user=PerevalUser.objects.create(
                email='Ivanov@mail.ru',
                surname='Иванов',
                name='Петр',
                otc='Васильевич',
                phone='89999999999'
            ),
            beauty_title='beauty_title',
            title='title',
            other_title='other_title',
            connect='connect',
            coord=PerevalCoordinate.objects.create(
                latitude=22.222,
                longitude=11.111,
                height=1000.0
            ),
            level=PerevalLevel.objects.create(
                winter='1a',
                summer='2a',
                autumn='3a',
                spring='4a'
            )
        )

        # Изображение для объекта перевал 1
        self.image_1 = Image.objects.create(
            title='Title_1',
            data='https://images.app.goo.gl/eT3kx7tigk33vNQG8',
            pereval=self.pereval_1
        )

        # Объект перевал 2
        self.pereval_2 = PerevalAdded.objects.create(
            user=PerevalUser.objects.create(
                email='Petrov@mail.ru',
                surname='Петров',
                name='Иван',
                otc='Васильевич',
                phone='89999998877'
            ),
            beauty_title='beauty_title2',
            title='title2',
            other_title='other_title2',
            connect='connect2',
            coord=PerevalCoordinate.objects.create(
                latitude=11.222,
                longitude=22.111,
                height=2000.0
            ),
            level=PerevalLevel.objects.create(
                winter='4a',
                summer='3a',
                autumn='2a',
                spring='1a'
            )
        )

        # Изображение для объекта перевал 2
        self.image_2 = Image.objects.create(
            title='Title_2',
            data='https://images.app.goo.gl/8JQJ8qgxTuFYCcRG7',
            pereval=self.pereval_2
        )

    def test_pereval_list(self):
        """Тест endpoint /perevals/ - список всех объектов модели PerevalAdded"""

        response = self.client.get(reverse('perevaladded-list'))
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_detail(self):
        """Тест endpoint /perevals/edit/{id} - объект модели PerevalAdded по его id"""

        response = self.client.get(reverse('perevaladded-detail', kwargs={'pk': self.pereval_1.id}))
        serializer_data = PerevalSerializer(self.pereval_1).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_user_email(self):
        """Тест endpoint /perevals/user__email=<email> - объекты модели PerevalAdded отфильтрованные по email пользователя"""

        email = self.pereval_1.user.email
        url = f'/perevals/?user__email={email}'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)