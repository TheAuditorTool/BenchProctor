# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from app_runtime import db


def BenchmarkTest14012(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
