# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from urllib.parse import unquote
import runpy


def BenchmarkTest18403(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
