# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest61911(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
