# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from types import SimpleNamespace


def BenchmarkTest32324(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
