
from .transcriber import youtube_transcribe
from .summarizer import transcription_summarize

async def handle():
    id = "RJjy7sJ8F0w"
    srt = await youtube_transcribe(id) 
    return transcription_summarize(srt)