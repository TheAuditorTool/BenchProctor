# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest79388(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    _resp = requests.get(str(origin_value))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
