# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from types import SimpleNamespace


def BenchmarkTest01892(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
