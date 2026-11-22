# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def validate_connector(request):
    summary = requests.get('https://api.partner.example.com/v1/profile').text
    handshake = (lambda v: v.strip())(summary)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(handshake).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
