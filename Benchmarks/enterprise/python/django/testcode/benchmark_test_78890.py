# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest78890(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
