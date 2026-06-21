# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import redis_client


def BenchmarkTest55751(request):
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = redis_value
            data = parsed
        case _:
            data = redis_value
    requests.get(str(data))
    return JsonResponse({"saved": True})
