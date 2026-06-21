# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest45740(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    os.remove(str(data))
    return JsonResponse({"saved": True})
