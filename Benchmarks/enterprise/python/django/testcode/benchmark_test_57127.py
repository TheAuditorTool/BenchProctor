# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from types import SimpleNamespace


def BenchmarkTest57127(request):
    multipart_value = request.POST.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
