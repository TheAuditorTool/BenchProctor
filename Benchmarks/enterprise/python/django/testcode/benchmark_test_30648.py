# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30648(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})
