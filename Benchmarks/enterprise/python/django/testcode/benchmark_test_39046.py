# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


def BenchmarkTest39046(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
