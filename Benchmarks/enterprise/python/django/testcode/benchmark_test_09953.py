# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import redis_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09953(request):
    redis_value = redis_client.get('user_data')
    ctx = RequestContext(redis_value)
    data = ctx.payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
