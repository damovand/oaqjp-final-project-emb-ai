'''

'''

import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
   # return (response.text)
    formatted_response = json.loads(response.text)
    
    predictions = formatted_response["emotionPredictions"]
    prediction = predictions[0]
    emotions = prediction["emotion"]
    if response.status_code == 200:
        max_score = 0 
        dominant_emotion = ""
        for key, value in emotions.items():
            if value > max_score:
                max_score = value
                dominant_emotion = key
    else:
        dominant_emotion = None
        #print(f" Found dominant {dominant_emotion} @ {max_score}")
    emotions['dominant_emotion']=dominant_emotion
    return (emotions)