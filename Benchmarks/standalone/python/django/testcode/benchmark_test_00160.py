# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00160(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return JsonResponse({'allocated': len(records)}, status=200)
