# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest33641(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
