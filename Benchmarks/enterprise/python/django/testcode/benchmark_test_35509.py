# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35509(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
