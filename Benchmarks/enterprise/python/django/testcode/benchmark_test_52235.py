# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import ast


def BenchmarkTest52235(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
