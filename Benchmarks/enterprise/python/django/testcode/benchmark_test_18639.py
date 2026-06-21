# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import redis_client


def BenchmarkTest18639(request):
    redis_value = redis_client.get('user_data')
    data = ' '.join(str(redis_value).split())
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
