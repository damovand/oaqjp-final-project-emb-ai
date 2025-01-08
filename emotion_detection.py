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
    formatted_response = json.loads(response.text)

    emotionPredictions = []
    emotions = []
    for key, value in formatted_response.items():
        if key == "emotionPredictions":
            emotionPredictions = value
           # print(f"Key: {key}, Value: {emotionPredictions}") 
        break
    prediction = emotionPredictions[0]
    for key, value in prediction.items():
        if key == "emotion":
            emotions = value
           # print(f"Key: {key}, Value: {emotionPredictions}") 
        break
    
    key_value_pairs =[]
    for k, v in emotions.items():
            key_value_pairs.append((k,v))
   # print(f"---------emotions {key_value_pairs}-----")
    return (key_value_pairs)