from django.urls import path

from softwareEngg.views import userInterface
from softwareEngg.views import pythonFullStake
from softwareEngg.views import reactNodeJs
from softwareEngg.views import javaFullStack


urlpatterns = [
    path('user/', userInterface),
    path('python/', pythonFullStake),
    path('react/', reactNodeJs),
    path('java/', javaFullStack),
]