# example/urls.py
from django.urls import path

from example.views import index, transcribe, summarize


urlpatterns = [
    path('', index),
    path('transcribe', transcribe),
    path('summarize', summarize)
]