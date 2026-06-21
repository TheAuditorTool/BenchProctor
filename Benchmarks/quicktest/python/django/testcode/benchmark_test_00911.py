# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00911(request):
    host_value = request.META.get('HTTP_HOST', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
