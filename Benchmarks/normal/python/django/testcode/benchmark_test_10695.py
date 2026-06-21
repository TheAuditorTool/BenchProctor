# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10695(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = handle(ua_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get('https://api.pycdn.io/data', params={'q': str(target_url)}, verify=False)
    return JsonResponse({"saved": True})
