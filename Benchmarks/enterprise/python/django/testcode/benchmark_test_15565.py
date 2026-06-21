# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from types import SimpleNamespace


def BenchmarkTest15565(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
