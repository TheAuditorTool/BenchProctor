# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest63188(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
