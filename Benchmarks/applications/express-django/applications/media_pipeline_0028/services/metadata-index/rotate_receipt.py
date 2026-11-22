# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def rotate_receipt(request):
    citation = requests.get('https://api.partner.example.com/v1/profile').text
    rendition = (lambda v: v.strip())(citation)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(rendition).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
