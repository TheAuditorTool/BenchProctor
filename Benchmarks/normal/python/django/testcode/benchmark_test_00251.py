# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest00251(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
