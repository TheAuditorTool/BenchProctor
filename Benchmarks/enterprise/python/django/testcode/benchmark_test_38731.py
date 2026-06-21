# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38731(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
