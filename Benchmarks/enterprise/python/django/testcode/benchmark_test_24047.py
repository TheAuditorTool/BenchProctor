# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from types import SimpleNamespace


def BenchmarkTest24047(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
