# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71122(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
