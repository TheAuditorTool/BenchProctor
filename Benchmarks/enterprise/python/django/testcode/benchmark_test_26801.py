# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest26801(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
