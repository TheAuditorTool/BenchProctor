# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest48667(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
