# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


def BenchmarkTest00064(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
