# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from types import SimpleNamespace


def BenchmarkTest74501(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
