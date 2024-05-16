import html
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import re

API_KEY = 'AQVNwFcVPVFWkZVbtKJ2X0avEgQhPMJSG-i301ey'
ENDPOINT = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'


@api_view(['POST'])
def generate(request):
    if request.method == 'POST':
        topic = request.data.get('topic')

        if not topic:
            return Response({'error': 'Topic is required'}, status=400)

        headers = {
            'Authorization': f'Api-Key  {API_KEY}',
            'Content-Type': 'application/json',
        }

        payload = {
            "modelUri": "gpt://b1gvfh06vnb75dsr235c/yandexgpt-lite/latest",
            "completionOptions": {
                "stream": False,
                "temperature": 0.3,
                "maxTokens": 500
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Ты — опытный анимешник. Предложи 3 манги в виде небольшого списка по переданным пользователем жанрам, передай с переносом строки и выдели жирым названия."
                },
                {
                    "role": "user",
                    "text": f"Привет, предложи мангу по заданному жанру: {topic}"
                }
            ]
        }

        response = requests.post(ENDPOINT, json=payload, headers=headers)
        print(response)
        if response.status_code == 200:
            # Парсим JSON ответ
            data = response.json()

            # Извлекаем текст из JSON
            text = data['result']['alternatives'][0]['message']['text']
            print(text)

            print(response.json())

            # Отправляем текст в ответе Django
            return JsonResponse({'text': text})

        else:
            # Если запрос завершился с ошибкой, возвращаем ошибку
            return JsonResponse({'error': 'Failed to generate text'}, status=response.status_code)


def bot_page(request):
    return render(request, 'mangabot/mangabot.html')