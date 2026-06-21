# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest64127(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
