import os
import requests

endpoint = "https://api.assemblyai.com/v2/transcript/{}".format(os.getenv("TRANSCRIPTION_ID"))

headers = {
    "authorization": os.getenv("ASSEMBLYAI_KEY"),
}

response = requests.get(endpoint, headers=headers)

print(response.json())
print("\n")
print(response.json()['text'])
