import argparse
import os
import requests
import sys
import time


API_URL = "https://api.assemblyai.com/v2/"
CDN_URL = "https://cdn.assemblyai.com/"


def initiate_transcription(file_id):
    """Sends a request to the API to transcribe a specific
    file that was previously uploaded to the API. This will
    not immediately return the transcription because it takes
    a moment for the service to analyze and perform the
    transcription, so there is a different function to retrieve
    the results.
    """
    endpoint = "".join([API_URL, "transcript"])
    json = {"audio_url": "".join([CDN_URL, "upload/{}".format(file_id)]), "content_safety": "true"}
    headers = {
        "authorization": os.getenv("ASSEMBLYAI_KEY"),
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_id")
    args = parser.parse_args()
    file_id = args.file_id
    response_json = initiate_transcription(file_id)
    print(response_json)

