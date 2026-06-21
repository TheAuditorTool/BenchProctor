# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from types import SimpleNamespace


def BenchmarkTest77555(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
