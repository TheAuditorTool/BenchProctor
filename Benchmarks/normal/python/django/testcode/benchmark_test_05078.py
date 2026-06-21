# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest05078(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed))
    return resp
