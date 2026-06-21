# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04543(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
