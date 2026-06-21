# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest59480(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
