# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00290(request):
    redis_value = redis_client.get('user_data')
    data = f'{redis_value!s}'
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
