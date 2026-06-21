# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest74401(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
