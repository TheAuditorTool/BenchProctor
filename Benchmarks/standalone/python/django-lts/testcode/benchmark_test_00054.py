# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00054(request):
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    User.objects.extra(where=['id = ' + str(processed)]).first()
    return JsonResponse({"saved": True})
