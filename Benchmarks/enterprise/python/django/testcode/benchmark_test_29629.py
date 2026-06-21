# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from types import SimpleNamespace


def BenchmarkTest29629(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
