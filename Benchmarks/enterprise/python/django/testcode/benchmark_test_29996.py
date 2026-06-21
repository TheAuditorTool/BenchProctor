# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest29996(request, path_param):
    path_value = path_param
    data = to_text(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
