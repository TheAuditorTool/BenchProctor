# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13138(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
