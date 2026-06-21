# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest19454(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
