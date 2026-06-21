# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09913(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
