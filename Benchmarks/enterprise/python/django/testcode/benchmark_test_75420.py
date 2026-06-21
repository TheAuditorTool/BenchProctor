# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest75420(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
