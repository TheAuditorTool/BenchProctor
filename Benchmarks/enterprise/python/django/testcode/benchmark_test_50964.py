# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import redis_client


def BenchmarkTest50964(request):
    redis_value = redis_client.get('user_data')
    data = '%s' % (redis_value,)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
