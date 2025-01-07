'''

'''

import requests, jsonify
import json
from flask import Flask, jsonify
def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    return (response.text)
    '''
    data = response.json()
    emotion_predictor = data.get('emotionPredictions')
    
    parsed_emotions = []
    for emotion in emotion_predictor:
        parsed_emotions.append({emotion})
    '''
    return jsonify(emotion_predictor)  # Return the response text from the API
    
        # Parsing the JSON response from the API
   # formatted_response = json.loads(response.text)

    #  I AM STUCK!
    