# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76151(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
