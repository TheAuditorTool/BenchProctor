# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65222(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
