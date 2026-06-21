# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


def BenchmarkTest19719(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
