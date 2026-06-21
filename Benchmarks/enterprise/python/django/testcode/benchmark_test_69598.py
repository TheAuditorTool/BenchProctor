# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest69598(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
