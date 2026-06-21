# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests
from types import SimpleNamespace


def BenchmarkTest61702(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
