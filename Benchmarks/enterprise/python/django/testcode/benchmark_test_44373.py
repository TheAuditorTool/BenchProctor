# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest44373(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
