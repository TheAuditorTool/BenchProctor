# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest67445(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
