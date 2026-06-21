# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53507(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
