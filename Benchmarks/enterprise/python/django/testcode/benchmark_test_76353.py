# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest76353(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
