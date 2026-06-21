# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest69004(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
