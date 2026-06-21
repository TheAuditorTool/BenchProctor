# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest16094(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = handle(auth_header)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
