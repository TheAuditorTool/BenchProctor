# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07741(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
