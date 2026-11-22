# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00059(request):
    redis_value = redis_client.get('user_data')
    data = '{}'.format(redis_value)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
