# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from types import SimpleNamespace


def BenchmarkTest80315(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
