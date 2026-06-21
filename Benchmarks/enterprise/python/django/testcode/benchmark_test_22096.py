# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest22096(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
