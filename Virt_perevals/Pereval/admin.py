from django.contrib import admin

from .models import PerevalUser, PerevalCoordinate, PerevalLevel, PerevalAdded, Image

admin.site.register(PerevalUser)
admin.site.register(PerevalCoordinate)
admin.site.register(PerevalLevel)
admin.site.register(PerevalAdded)
admin.site.register(Image)