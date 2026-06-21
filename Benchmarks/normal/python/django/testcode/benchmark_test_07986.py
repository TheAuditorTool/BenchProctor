# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest07986(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    def _primary():
        exec(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
