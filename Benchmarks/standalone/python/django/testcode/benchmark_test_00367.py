# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00367(request):
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    requests.get(str(data))
    return JsonResponse({"saved": True})
