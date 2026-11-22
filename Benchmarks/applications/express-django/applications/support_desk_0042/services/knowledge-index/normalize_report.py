# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def normalize_report(request):
    blurb = requests.get('https://api.partner.example.com/v1/profile').text
    inquiry = (lambda v: v.strip())(blurb)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(inquiry).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
