# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import redis_client


def BenchmarkTest39517(request):
    redis_value = redis_client.get('user_data')
    data = redis_value if redis_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
