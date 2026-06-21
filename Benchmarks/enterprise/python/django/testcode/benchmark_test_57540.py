# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest57540(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
