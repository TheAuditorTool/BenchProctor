# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import os
from types import SimpleNamespace


def BenchmarkTest20675(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
