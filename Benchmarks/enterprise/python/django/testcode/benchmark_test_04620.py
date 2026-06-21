# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib
import sys


def BenchmarkTest04620(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
