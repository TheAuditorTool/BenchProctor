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

def BenchmarkTest31336(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
