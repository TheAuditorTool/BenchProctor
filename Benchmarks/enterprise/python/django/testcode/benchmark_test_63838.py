# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import runpy


def relay_value(value):
    return value

def BenchmarkTest63838(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
