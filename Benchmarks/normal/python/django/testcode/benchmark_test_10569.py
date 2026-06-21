# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10569(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
