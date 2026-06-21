# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest51022(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
