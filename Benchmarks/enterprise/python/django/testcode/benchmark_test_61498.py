# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest61498(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
