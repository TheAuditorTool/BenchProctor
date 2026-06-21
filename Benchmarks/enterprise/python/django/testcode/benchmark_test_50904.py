# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from types import SimpleNamespace


def BenchmarkTest50904(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
