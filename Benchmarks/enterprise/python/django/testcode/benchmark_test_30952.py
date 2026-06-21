# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest30952(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
