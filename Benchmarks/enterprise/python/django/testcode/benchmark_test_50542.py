# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
import runpy


def BenchmarkTest50542(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
