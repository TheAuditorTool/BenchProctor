# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest22173(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
