# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def merge_window(request):
    preface = requests.get('https://api.partner.example.com/v1/profile').text
    grievance = (lambda v: v.strip())(preface)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(grievance).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
