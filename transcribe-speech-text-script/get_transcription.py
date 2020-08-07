import argparse
import os
import requests
import sys
import time


API_URL = "https://api.assemblyai.com/v2/"


def get_transcription(transcription_id):
    """Requests the transcription from the API and returns the JSON
    response."""
    endpoint = "".join([API_URL, "transcript/{}".format(transcription_id)])
    headers = {"authorization": os.getenv('ASSEMBLYAI_KEY')}
    response = requests.get(endpoint, headers=headers)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("transcription_id")
    args = parser.parse_args()
    transcription_id = args.transcription_id
    response_json = get_transcription(transcription_id)
    for word in response_json['words']:
        print(word['text'], end=" ")
