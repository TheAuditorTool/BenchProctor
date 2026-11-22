# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
import os


def BenchmarkTest00169(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
