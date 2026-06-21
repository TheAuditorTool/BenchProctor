# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import hashlib
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest21829(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JsonResponse({'error': 'integrity check failed'}, status=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
