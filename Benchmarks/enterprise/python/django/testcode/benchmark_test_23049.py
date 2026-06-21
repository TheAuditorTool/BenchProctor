# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest23049(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    importlib.import_module(str(forwarded_ip))
    return JsonResponse({"saved": True})
