# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
from app_runtime import db


def BenchmarkTest39338(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
