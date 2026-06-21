# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from types import SimpleNamespace


def BenchmarkTest49049(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
