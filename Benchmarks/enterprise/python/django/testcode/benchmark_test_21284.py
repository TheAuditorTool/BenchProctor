# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest21284(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
