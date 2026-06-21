# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest59854(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    sys.path.insert(0, str(ua_value))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
