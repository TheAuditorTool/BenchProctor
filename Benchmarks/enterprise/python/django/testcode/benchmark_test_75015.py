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

def BenchmarkTest75015(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    return HttpResponse(str(data), content_type='text/html')
