# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39446(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
