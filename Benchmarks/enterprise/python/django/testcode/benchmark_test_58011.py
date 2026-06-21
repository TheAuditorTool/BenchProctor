# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
from types import SimpleNamespace


def BenchmarkTest58011(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
