# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import time
from types import SimpleNamespace


def BenchmarkTest74172(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
