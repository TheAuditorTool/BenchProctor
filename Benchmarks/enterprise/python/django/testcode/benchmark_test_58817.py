# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import importlib
import sys


def BenchmarkTest58817(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
