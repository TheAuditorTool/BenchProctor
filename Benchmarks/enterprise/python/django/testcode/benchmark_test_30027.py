# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest30027(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
