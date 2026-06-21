# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36434(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
