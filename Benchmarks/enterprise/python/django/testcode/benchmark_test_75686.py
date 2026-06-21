# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest75686(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
