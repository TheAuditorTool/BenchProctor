# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest12045(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ensure_str(referer_value)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
