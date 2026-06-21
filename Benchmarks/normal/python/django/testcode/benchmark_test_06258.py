# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06258(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
