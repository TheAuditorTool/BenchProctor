# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest49279(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
