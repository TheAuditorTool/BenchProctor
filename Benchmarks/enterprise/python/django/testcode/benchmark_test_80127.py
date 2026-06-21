# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest80127(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
