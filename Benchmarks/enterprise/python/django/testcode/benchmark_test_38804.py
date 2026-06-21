# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest38804(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    importlib.import_module(str(origin_value))
    return JsonResponse({"saved": True})
