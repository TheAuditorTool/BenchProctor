# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest71549(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
