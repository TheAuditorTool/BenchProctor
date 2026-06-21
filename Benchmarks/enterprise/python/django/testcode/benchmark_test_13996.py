# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13996(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
