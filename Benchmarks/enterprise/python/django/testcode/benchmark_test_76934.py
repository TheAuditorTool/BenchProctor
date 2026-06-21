# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import base64
from app_runtime import redis_client


def BenchmarkTest76934(request):
    redis_value = redis_client.get('user_data')
    data = base64.b64decode(redis_value).decode('utf-8', 'ignore')
    json.loads(data)
    return JsonResponse({"saved": True})
