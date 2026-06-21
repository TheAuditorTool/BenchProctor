# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import redis_client


def BenchmarkTest67300(request):
    redis_value = redis_client.get('user_data')
    try:
        data = json.loads(redis_value).get('value', redis_value)
    except (json.JSONDecodeError, AttributeError):
        data = redis_value
    json.loads(data)
    return JsonResponse({"saved": True})
