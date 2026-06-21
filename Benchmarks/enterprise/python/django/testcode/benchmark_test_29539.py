# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import redis_client


def BenchmarkTest29539(request):
    redis_value = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    data = normalize(redis_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
