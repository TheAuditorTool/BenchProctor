# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest81140(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(target_url)})
