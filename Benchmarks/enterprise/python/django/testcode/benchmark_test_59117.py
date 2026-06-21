# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59117(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
