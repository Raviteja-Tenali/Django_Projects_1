from django.urls import path

from civilEngg.views import autoCad
from civilEngg.views import totalStation
from civilEngg.views import estimations
from civilEngg.views import raviclass

urlpatterns = [
    path('autocad/', autoCad),
    path('totalstation/', totalStation),
    path('estimations/', estimations),
    path('ravi/',raviclass.as_view()),
]