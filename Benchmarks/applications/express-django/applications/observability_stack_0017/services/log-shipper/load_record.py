# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import requests


@csrf_exempt
def load_record(request):
    note = requests.get('https://api.partner.example.com/v1/profile').text
    cohort = (lambda v: v.strip())(note)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(cohort).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
