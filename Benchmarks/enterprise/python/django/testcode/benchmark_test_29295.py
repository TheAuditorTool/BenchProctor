# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import redis_client


def BenchmarkTest29295(request):
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
