# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest04929(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ensure_str(ua_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
