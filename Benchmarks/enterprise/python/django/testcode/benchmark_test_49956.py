# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle
from app_runtime import redis_client


def BenchmarkTest49956(request):
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
