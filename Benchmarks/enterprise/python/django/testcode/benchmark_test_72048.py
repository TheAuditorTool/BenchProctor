# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest72048(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    os.remove(str(data))
    return JsonResponse({"saved": True})
