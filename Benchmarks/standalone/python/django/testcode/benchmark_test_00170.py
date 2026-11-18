# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00170(request):
    redis_value = redis_client.get('user_data')
    data = f'{redis_value!s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
