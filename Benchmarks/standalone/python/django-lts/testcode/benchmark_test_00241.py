# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00241(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return JsonResponse({'allocated': len(records)}, status=200)
