# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest80335(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
