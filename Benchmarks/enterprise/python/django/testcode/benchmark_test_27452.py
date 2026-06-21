# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from types import SimpleNamespace


def BenchmarkTest27452(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
