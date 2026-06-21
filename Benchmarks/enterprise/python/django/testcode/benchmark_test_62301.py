# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import hashlib
from app_runtime import db


def BenchmarkTest62301(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JsonResponse({'error': 'integrity check failed'}, status=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
