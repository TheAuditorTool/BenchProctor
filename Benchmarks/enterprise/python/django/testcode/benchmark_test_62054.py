# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62054(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
