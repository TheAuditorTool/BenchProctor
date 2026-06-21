# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace


def BenchmarkTest47154(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return JsonResponse({"saved": True})
