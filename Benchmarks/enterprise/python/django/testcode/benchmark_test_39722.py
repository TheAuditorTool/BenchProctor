# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest39722(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
