# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import redis_client


def BenchmarkTest62100(request):
    redis_value = redis_client.get('user_data')
    data = (lambda v: v.strip())(redis_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
