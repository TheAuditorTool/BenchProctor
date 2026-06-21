# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib
import sys
from types import SimpleNamespace


def BenchmarkTest39001(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
