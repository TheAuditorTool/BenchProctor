# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import redis_client


def relay_value(value):
    return value

def BenchmarkTest33640(request):
    redis_value = redis_client.get('user_data')
    data = relay_value(redis_value)
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return JsonResponse({"saved": True})
