# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def validate_receipt(request):
    caption = requests.get('https://api.partner.example.com/v1/profile').text
    remittance = (lambda v: v.strip())(caption)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(remittance).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
