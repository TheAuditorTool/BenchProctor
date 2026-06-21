# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from types import SimpleNamespace


def BenchmarkTest67498(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
