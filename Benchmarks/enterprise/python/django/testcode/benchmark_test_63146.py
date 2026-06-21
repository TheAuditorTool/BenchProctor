# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63146(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
