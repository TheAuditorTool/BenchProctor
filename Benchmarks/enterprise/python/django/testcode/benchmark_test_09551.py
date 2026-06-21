# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import requests
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09551(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get('https://api.pycdn.io/data', params={'q': str(target_url)}, verify=False)
    return JsonResponse({"saved": True})
