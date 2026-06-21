# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import runpy


def BenchmarkTest25685(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
