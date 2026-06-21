# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def normalise_input(value):
    return value.strip()

def BenchmarkTest79620(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
