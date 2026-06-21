# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest49879(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
