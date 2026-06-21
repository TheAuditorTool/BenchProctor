# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10083(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
