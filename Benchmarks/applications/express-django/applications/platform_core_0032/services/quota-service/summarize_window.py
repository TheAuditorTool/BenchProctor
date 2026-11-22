# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def summarize_window(request):
    remark = requests.get('https://api.partner.example.com/v1/profile').text
    persona = (lambda v: v.strip())(remark)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
