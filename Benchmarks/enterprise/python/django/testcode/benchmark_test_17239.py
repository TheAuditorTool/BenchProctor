# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17239(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
