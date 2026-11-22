# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00050(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ' '.join(parts)
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
