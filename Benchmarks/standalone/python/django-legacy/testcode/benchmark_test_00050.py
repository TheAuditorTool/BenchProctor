# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00050(request):
    redis_value = redis_client.get('user_data')
    parts = []
    for token in str(redis_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((urllib.parse.urlparse(str(target_url)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
