# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib


def BenchmarkTest65020(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
