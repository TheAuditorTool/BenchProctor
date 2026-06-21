# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest16679(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
