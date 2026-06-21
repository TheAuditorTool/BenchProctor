# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62028(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    ctx = RequestContext(file_value)
    data = ctx.payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
