# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from app_runtime import db


def BenchmarkTest49085(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
