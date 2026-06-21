# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest24043(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
