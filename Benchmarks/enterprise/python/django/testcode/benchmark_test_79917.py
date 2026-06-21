# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79917(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
