# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00056(request):
    redis_value = redis_client.get('user_data')
    data = str(redis_value).replace('\x00', '')
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
