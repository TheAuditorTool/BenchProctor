# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
from types import SimpleNamespace


def BenchmarkTest08831(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
