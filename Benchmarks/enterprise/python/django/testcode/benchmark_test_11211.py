# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import redis_client


def BenchmarkTest11211(request):
    redis_value = redis_client.get('user_data')
    data = f'{redis_value:.200s}'
    json.loads(data)
    return JsonResponse({"saved": True})
