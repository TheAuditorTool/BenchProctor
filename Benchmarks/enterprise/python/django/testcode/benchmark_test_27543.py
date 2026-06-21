# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json
from types import SimpleNamespace


def BenchmarkTest27543(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})
