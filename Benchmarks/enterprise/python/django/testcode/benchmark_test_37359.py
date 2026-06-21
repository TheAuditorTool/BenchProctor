# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37359(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
