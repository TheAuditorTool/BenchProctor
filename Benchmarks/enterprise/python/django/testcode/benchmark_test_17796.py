# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17796(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    ctx = RequestContext(secret_value)
    data = ctx.payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
