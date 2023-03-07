import os
import openai
import tiktoken

openai.api_key = os.getenv("OPENAI_API_KEY")
gpt3Encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def transcription_summarize(text):
    num_tokens = num_tokens_from_string(text, gpt3Encoding.name)
    if num_tokens > 4096 - 512:
        return "Text too long"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": generate_prompt()},
            {"role": "user", "content": text},
        ],
        temperature=0,
        n=1,
        presence_penalty=2,
        frequency_penalty=2,
        max_tokens=512,
    )

    return response['choices'][0]['message']['content']

def generate_prompt():
    return """ 
You are specialist in summarizing textual information provided to you. 
You need to summarize transcribed text that is extracted from a youtube video. Skip all the unnecessary information, adverisements, sponsored parts, etc.

Expected response markdown format:
Title: [title of the summary]
Key Points: [bullet list of main takeway points]
Summary: [Detailed summary of the transcribed text explained concisely]

User provides the input
"""
