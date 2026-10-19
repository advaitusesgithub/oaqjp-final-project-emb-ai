# import requests


# def emotion_detector(text_to_analyze):
#     url = (
#         "https://sn-watson-emotion.labs.skills.network/"
#         "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
#     )

#     headers = {
#         "grpc-metadata-mm-model-id":
#             "emotion_aggregated-workflow_lang_en_stock"
#     }

#     payload = {
#         "raw_document": {
#             "text": text_to_analyze
#         }
#     }

#     response = requests.post(
#         url,
#         json=payload,
#         headers=headers
#     )

#     return response.text


# import json
# import requests


# def emotion_detector(text_to_analyze):
#     """Detect emotions and return scores and the dominant emotion."""
#     url = (
#         "https://sn-watson-emotion.labs.skills.network/"
#         "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
#     )

#     headers = {
#         "grpc-metadata-mm-model-id":
#             "emotion_aggregated-workflow_lang_en_stock"
#     }

#     payload = {
#         "raw_document": {
#             "text": text_to_analyze
#         }
#     }

#     response = requests.post(
#         url,
#         json=payload,
#         headers=headers
#     )

#     formatted_response = json.loads(response.text)
#     emotions = formatted_response["emotionPredictions"][0]["emotion"]

#     anger_score = emotions["anger"]
#     disgust_score = emotions["disgust"]
#     fear_score = emotions["fear"]
#     joy_score = emotions["joy"]
#     sadness_score = emotions["sadness"]

#     scores = {
#         "anger": anger_score,
#         "disgust": disgust_score,
#         "fear": fear_score,
#         "joy": joy_score,
#         "sadness": sadness_score
#     }

#     dominant_emotion = max(scores, key=scores.get)

#     scores["dominant_emotion"] = dominant_emotion

#     return scores

import json
import requests


def emotion_detector(text_to_analyze):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"]
    }
    scores["dominant_emotion"] = max(scores, key=scores.get)

    return scores