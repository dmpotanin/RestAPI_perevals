from django.db import models


LEVEL_LIST = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
]


class PerevalUser(models.Model):
    """Пользователь"""

    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    otc = models.CharField(max_length=255, verbose_name='Отчество')
    email = models.CharField(max_length=255, verbose_name='Почта')
    phone = models.CharField(max_length=255, verbose_name='Телефон')

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class PerevalCoordinate(models.Model):
    """Координаты"""

    latitude = models.FloatField(max_length=30, verbose_name='Широта')
    longitude = models.FloatField(max_length=30, verbose_name='Долгота')
    height = models.FloatField(max_length=20, verbose_name='Высота')

    def __str__(self):
        return f'широта:{self.latitude}, долгота:{self.longitude}, высота:{self.height}'


class PerevalLevel(models.Model):
    """Уровень сложности по сезонам"""

    winter = models.CharField(max_length=2, choices=LEVEL_LIST, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=2, choices=LEVEL_LIST, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=2, choices=LEVEL_LIST, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=2, choices=LEVEL_LIST, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        l_winter = f'Зима - {self.winter};' if self.winter else ""
        l_summer = f'Лето - {self.summer};' if self.summer else ""
        l_autumn = f'Осень - {self.autumn};' if self.autumn else ""
        l_spring = f'Весна - {self.spring};' if self.spring else ""

        return f'{l_winter} {l_summer} {l_autumn} {l_spring}'


class PerevalAdded(models.Model):
    """Перевал"""

    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'

    STATUS_LIST = (
        ('NW', 'New'),
        ('AC', 'Accepted'),
        ('PN', 'Pending'),
        ('RJ', 'Rejected'),
    )

    beauty_title = models.CharField(max_length=255, verbose_name='Индекс')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_title = models.CharField(max_length=255, verbose_name='Другое название', null=True, blank=True)
    connect = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_LIST, default=NEW)
    coord = models.OneToOneField(PerevalCoordinate, on_delete=models.CASCADE)
    user = models.ForeignKey(PerevalUser, on_delete=models.CASCADE)
    level = models.ForeignKey(PerevalLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.beauty_title}, {self.title}'

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"


class Image(models.Model):
    """Изображение"""

    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    data = models.ImageField(verbose_name='Название', null=True, blank=True)
    pereval = models.ForeignKey(PerevalAdded, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'