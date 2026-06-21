# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def relay_value(value):
    return value

def BenchmarkTest55810(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
