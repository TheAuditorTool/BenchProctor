# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest75422(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    sys.path.insert(0, str(auth_header))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
