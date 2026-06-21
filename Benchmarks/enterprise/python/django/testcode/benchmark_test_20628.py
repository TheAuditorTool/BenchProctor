# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def normalise_input(value):
    return value.strip()

def BenchmarkTest20628(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
