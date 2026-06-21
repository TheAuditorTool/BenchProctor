# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12316(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
