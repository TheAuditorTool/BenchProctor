# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib
from types import SimpleNamespace


def BenchmarkTest31190(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
