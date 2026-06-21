# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes
from types import SimpleNamespace


def BenchmarkTest56596(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
