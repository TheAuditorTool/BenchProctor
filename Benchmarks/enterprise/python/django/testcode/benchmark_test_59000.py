# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59000(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return JsonResponse({"saved": True})
