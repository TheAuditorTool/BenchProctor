# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import re
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00111(request):
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ' '.join(parts)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
