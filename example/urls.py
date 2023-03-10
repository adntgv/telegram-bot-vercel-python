# example/urls.py
from django.urls import path

from example.views import index, transcribe, summarize, handle


urlpatterns = [
    path('', index),
    path('transcribe', transcribe),
    path('summarize', summarize),
    path('handle', handle)
]