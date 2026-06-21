# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from types import SimpleNamespace


def BenchmarkTest06446(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
