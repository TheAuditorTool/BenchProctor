# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41599(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
