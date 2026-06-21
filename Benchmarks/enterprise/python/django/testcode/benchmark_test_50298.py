# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def normalise_input(value):
    return value.strip()

def BenchmarkTest50298(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
