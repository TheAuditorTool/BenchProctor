# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import redis_client


def BenchmarkTest41426(request):
    redis_value = redis_client.get('user_data')
    data = '%s' % str(redis_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
