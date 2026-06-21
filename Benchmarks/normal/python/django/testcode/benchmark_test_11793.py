# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11793(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
