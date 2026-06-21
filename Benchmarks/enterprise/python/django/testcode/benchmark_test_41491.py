# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from types import SimpleNamespace


def BenchmarkTest41491(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
