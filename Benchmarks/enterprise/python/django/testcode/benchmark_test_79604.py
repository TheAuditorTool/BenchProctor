# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79604(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
