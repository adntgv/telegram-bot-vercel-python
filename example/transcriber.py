from youtube_transcript_api import YouTubeTranscriptApi

async def youtube_transcribe(id):
    srt = YouTubeTranscriptApi.get_transcript(id)

    res = ""
    for item in srt:
        res += f"{item['text']} "
    return res
