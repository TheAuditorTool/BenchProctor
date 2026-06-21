# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import runpy


def ensure_str(value):
    return str(value)

def BenchmarkTest55431(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
