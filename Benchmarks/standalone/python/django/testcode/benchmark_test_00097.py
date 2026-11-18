# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00097(request):
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(redis_value).strip()
        case _:
            data = str(redis_value)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
