# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
import hashlib
from app_runtime import db


def BenchmarkTest19980(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JsonResponse({'error': 'integrity check failed'}, status=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
