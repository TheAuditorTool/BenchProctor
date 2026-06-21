# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest21061(request, path_param):
    path_value = path_param
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(path_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
