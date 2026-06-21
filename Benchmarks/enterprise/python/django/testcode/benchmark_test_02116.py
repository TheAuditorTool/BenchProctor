# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import redis_client


def BenchmarkTest02116(request):
    redis_value = redis_client.get('user_data')
    pickle.loads(redis_value.encode('latin-1'))
    return JsonResponse({"saved": True})
