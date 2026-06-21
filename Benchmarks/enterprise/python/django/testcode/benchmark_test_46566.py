# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46566(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
