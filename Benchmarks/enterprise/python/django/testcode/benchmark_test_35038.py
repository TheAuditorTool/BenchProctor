# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from types import SimpleNamespace


def BenchmarkTest35038(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
