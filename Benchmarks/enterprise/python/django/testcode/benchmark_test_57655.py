# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest57655(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
