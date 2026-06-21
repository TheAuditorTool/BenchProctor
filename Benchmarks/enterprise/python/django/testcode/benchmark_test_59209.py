# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest59209(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JsonResponse({'lookup': arr[idx]}, status=200)
