# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import redis_client


def BenchmarkTest01832(request):
    redis_value = redis_client.get('user_data')
    data = redis_value if redis_value else 'default'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
