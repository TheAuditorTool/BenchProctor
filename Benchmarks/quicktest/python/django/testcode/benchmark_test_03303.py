# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest03303(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
