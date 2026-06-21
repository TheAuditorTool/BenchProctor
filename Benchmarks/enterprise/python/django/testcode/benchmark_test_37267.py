# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37267(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
