import os
import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": os.getenv("RECORDING_URL")
}

headers = {
    "authorization": os.getenv("ASSEMBLYAI_KEY"),
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

print(response.json())
