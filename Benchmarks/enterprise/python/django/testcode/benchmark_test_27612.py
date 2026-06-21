# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest27612(request):
    host_value = request.META.get('HTTP_HOST', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(host_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = host_value
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
