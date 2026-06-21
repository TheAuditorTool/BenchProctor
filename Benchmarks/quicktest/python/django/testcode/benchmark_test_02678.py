# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import redis_client


def BenchmarkTest02678(request):
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
