# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00076(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
