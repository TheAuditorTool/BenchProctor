# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re


def BenchmarkTest19885(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
