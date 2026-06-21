# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest46027(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    sys.path.insert(0, str(forwarded_ip))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
