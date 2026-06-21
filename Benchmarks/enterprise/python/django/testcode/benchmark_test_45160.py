# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from types import SimpleNamespace


def BenchmarkTest45160(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
