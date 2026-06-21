# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from types import SimpleNamespace


def BenchmarkTest33561(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return JsonResponse({"saved": True})
