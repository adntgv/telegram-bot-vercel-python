# example/urls.py
from django.urls import path

from example.views import index, transcribe


urlpatterns = [
    path('', index),
    path('transcribe', transcribe)
]