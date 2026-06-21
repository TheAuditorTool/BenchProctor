# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib
import sys


def relay_value(value):
    return value

def BenchmarkTest38098(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
