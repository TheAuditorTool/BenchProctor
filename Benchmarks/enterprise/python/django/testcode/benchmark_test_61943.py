# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import re


def BenchmarkTest61943(request):
    secret_value = 'config_secret_test_abc123'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return JsonResponse({"saved": True})
