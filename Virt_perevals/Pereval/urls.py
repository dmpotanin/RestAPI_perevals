from django.urls import path, include

from rest_framework import routers

from Pereval.views import PerevalViewset, PerevalListView

create_pereval = routers.DefaultRouter()
create_pereval.register(r'', PerevalViewset)

urlpatterns = [
    path('perevals/', PerevalListView.as_view()),
    path('perevals/create/', include(create_pereval.urls)),
]