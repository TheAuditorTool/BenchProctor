# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00142(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value!s}'
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
