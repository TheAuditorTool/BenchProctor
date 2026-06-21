# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest33381(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    def _primary():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
