# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest28821(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
