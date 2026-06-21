# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from types import SimpleNamespace


def BenchmarkTest23919(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
