# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
from app_runtime import redis_client


def BenchmarkTest19064(request):
    redis_value = redis_client.get('user_data')
    try:
        data = json.loads(redis_value).get('value', redis_value)
    except (json.JSONDecodeError, AttributeError):
        data = redis_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
