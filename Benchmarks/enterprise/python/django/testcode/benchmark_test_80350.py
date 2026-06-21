# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest80350(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
