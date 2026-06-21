# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from types import SimpleNamespace


def BenchmarkTest14859(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
