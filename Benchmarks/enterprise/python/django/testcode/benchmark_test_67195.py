# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import runpy


def BenchmarkTest67195(request):
    host_value = request.META.get('HTTP_HOST', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', host_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = host_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
