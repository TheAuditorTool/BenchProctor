# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import hashlib
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15848(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JsonResponse({'error': 'integrity check failed'}, status=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
