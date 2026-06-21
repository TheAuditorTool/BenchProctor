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

def BenchmarkTest80089(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = handle(header_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
