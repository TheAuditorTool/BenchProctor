# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55537(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
