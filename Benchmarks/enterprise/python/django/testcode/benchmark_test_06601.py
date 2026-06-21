# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06601(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
