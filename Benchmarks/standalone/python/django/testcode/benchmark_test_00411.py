# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re
import os
import redis


def make_reader(raw):
    def read():
        return raw.strip()
    return read
redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00411(request):
    redis_value = redis_client.get('user_data')
    reader = make_reader(redis_value)
    data = reader()
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
