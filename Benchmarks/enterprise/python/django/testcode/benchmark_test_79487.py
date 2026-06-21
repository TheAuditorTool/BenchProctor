# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79487(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
