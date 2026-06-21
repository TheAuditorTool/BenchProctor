# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def relay_value(value):
    return value

def BenchmarkTest77734(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
