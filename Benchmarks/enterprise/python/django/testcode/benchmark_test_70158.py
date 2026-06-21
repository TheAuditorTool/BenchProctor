# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest70158(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
