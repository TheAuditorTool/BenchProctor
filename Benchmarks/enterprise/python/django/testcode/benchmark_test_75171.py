# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest75171(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
