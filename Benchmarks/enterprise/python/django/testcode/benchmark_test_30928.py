# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from types import SimpleNamespace


def BenchmarkTest30928(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
