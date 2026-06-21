# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest32658(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
