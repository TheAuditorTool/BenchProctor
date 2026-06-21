# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest01165(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    return HttpResponse(str(data), content_type='text/html')
