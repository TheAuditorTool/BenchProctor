# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06516(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
