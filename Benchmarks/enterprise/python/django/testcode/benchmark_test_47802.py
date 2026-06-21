# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from types import SimpleNamespace


def BenchmarkTest47802(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
