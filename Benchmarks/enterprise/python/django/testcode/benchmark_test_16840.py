# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest16840(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
