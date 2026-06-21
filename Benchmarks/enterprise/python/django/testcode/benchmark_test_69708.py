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

def BenchmarkTest69708(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
