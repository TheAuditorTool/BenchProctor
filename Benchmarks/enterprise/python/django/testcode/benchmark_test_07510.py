# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from types import SimpleNamespace


def BenchmarkTest07510(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
