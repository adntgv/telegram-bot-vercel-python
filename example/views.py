import asyncio
import json
from django.http import HttpResponse
from .bot import bot_tele
from .transcriber import youtube_transcribe
from .summarizer import transcription_summarize
from .app import handle as h


def index(request):
    if request.method == 'POST':
        data = request.body
        res = json.loads(data.decode('utf-8'))
        print(res)
        asyncio.run(bot_tele(res))
        return HttpResponse("ok")
    else:
        return HttpResponse("hello world!")


def transcribe(request):
    id = request.GET.get('id')
    return HttpResponse(asyncio.run(youtube_transcribe(id)))


def summarize(request):
    id = request.GET.get('id')
    transcription = asyncio.run(youtube_transcribe(id))
    summary = transcription_summarize(transcription)
    return HttpResponse(summary)

def handle(request):
    id = request.GET.get('id')
    summary = asyncio.run(h(id)) 
    return HttpResponse(summary)