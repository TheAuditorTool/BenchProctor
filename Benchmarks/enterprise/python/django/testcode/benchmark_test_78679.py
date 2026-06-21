# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import redis_client


def coalesce_blank(value):
    return value or ''

def BenchmarkTest78679(request):
    redis_value = redis_client.get('user_data')
    data = coalesce_blank(redis_value)
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
