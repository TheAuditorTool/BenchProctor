# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest67830(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ctx = RequestContext(prop_value)
    data = ctx.payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
