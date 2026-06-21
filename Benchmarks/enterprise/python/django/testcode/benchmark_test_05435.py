# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05435(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
