# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18038(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
