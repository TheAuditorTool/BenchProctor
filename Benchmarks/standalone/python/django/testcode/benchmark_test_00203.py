# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00203(request):
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ' '.join(parts)
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)
