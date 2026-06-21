# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import hashlib
from app_runtime import db


def BenchmarkTest43365(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JsonResponse({'error': 'integrity check failed'}, status=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
