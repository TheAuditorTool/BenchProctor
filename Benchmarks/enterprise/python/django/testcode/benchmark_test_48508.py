# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest48508(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = handle(auth_header)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
