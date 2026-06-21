# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import re
import ast


def BenchmarkTest31327(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
