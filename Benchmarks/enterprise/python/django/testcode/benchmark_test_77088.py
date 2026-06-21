# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest77088(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    sys.path.insert(0, str(referer_value))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
