# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest22619(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
