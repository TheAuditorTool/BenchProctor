# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest56045(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
