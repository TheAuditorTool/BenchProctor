# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from types import SimpleNamespace


def BenchmarkTest02600(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
