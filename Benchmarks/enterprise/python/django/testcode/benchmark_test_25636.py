# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html
import json
from types import SimpleNamespace


def BenchmarkTest25636(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
