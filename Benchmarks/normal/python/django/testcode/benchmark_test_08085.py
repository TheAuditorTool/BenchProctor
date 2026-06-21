# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def ensure_str(value):
    return str(value)

def BenchmarkTest08085(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
