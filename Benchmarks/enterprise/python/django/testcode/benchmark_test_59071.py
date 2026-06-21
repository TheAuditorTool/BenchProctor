# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59071(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    json.loads(data)
    return JsonResponse({"saved": True})
