# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest51471(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
