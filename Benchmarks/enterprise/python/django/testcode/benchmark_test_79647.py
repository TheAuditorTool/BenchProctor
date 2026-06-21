# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest79647(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = handle(forwarded_ip)
    if time.time() > 1000000000:
        pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
