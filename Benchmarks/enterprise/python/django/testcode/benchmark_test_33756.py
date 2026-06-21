# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest33756(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
