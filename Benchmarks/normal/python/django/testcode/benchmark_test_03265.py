# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03265(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
