# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest27991(request):
    raw_body = request.body.decode('utf-8')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(raw_body) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
