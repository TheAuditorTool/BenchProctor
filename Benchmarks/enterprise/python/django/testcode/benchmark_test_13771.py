# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from types import SimpleNamespace
from app_runtime import redis_client


def BenchmarkTest13771(request):
    redis_value = redis_client.get('user_data')
    ns = SimpleNamespace(payload=redis_value)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
