# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46197(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
