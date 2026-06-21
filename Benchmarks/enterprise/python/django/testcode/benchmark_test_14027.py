# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import runpy


def BenchmarkTest14027(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', origin_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = origin_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
