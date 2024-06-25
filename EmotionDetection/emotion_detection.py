import requests
import json
def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)
   formatted_response = json.loads(response.text)
   if response.status_code == 200:
    prediction = formatted_response['emotionPredictions'][0]['emotion']
    dominant_value = max(prediction.values())
    for k,v in prediction.items():
        if v == dominant_value:
            dominant_emotion = k
            break
    prediction['dominant_emotion'] = dominant_emotion
    return prediction
   return None