# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest58119(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
