# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest79346(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = to_text(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
