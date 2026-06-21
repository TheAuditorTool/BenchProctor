# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import redis_client


def BenchmarkTest42661(request):
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
