# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest10366(request):
    cookie_value = request.COOKIES.get('session_token', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(cookie_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
