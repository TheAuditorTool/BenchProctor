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

def BenchmarkTest10624(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
