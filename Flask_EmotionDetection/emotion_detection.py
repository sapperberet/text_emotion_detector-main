import requests
import json
def emotion_detector(text_to_analyse):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    object = { "raw_document": { "text": text_to_analyse } } 
    response = requests.post(URL,headers=Headers,json=object)
    if response.status_code == 200:
        fresponse = json.loads(response.text)
        emotions = fresponse['emotionPredictions'][0]['emotion']
        angerScore= emotions['anger']
        disgustScore= emotions['disgust']
        fearScore= emotions['fear']
        joyScore= emotions['joy']
        sadnessScore= emotions['sadness']
        mostemotion = max(emotions, key=emotions.get)
        return     {
        'anger': angerScore,
        'disgust': disgustScore,
        'fear': fearScore,
        'joy': joyScore,
        'sadness': sadnessScore,
        'dominant_emotion': mostemotion
        }
