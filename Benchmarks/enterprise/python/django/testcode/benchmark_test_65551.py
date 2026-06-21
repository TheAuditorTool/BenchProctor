# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65551(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
