# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest28463(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    sys.path.insert(0, str(origin_value))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
