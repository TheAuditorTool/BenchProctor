# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest28869(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
