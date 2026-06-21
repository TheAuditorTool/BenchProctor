# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest33143(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
