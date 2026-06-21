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

def BenchmarkTest04074(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
