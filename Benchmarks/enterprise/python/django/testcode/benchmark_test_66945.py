# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest66945(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(cookie_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = cookie_value
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
