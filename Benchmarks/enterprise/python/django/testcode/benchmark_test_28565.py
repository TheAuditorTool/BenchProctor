# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from types import SimpleNamespace


def BenchmarkTest28565(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
