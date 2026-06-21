# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest20592(request):
    host_value = request.META.get('HTTP_HOST', '')
    sys.path.insert(0, str(host_value))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
