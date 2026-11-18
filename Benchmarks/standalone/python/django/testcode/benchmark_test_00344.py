# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00344(request):
    redis_value = redis_client.get('user_data')
    data = str(redis_value).replace('\x00', '')
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
