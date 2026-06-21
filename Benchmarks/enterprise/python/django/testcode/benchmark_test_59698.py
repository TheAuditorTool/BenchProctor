# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import runpy


def BenchmarkTest59698(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
