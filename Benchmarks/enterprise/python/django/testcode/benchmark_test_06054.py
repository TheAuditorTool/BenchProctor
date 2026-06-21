# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def normalise_input(value):
    return value.strip()

def BenchmarkTest06054(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
