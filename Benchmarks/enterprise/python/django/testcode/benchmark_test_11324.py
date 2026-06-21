# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import runpy


def BenchmarkTest11324(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
