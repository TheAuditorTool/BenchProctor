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

def BenchmarkTest15807(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})
