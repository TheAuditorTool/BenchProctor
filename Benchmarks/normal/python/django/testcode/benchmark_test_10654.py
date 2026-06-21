# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10654(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
