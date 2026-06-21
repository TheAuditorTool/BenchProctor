# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace


def BenchmarkTest62393(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return JsonResponse({"saved": True})
