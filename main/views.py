import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings


from .functions import *
# Create your views here.


def welcome(request):

    token = settings.WHATSAPP_TOKEN
    return render(request, 'business/index.html', {'token': token})


@csrf_exempt
def whatsappWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'test'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']

                        # phoneNumber = '254706551542'
                        message = 'RE: {} test was received'.format(text)
                        sendWhatsappMessage(fromId, message)

                        # handleWhatsappChat(fromId, profileName, phoneId, text)
                except:
                    pass

        return HttpResponse('success', status=200)
