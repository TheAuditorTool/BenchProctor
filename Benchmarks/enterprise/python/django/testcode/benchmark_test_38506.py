# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest38506(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
