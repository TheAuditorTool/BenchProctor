# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import runpy


request_state: dict[str, str] = {}

def BenchmarkTest22390(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
