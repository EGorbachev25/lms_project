from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from telegram.service import send_telegram_message


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def telegram(request: Request):
    data = request.data
    chat_id = data['message']['chat']['id']
    text = "Hello from Django Bot!"
    send_telegram_message(chat_id, text)
    return Response({"status": "success"})

