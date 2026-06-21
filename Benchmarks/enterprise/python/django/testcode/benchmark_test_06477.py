# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from types import SimpleNamespace


def BenchmarkTest06477(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
