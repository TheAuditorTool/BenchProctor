# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest10169(request):
    raw_body = request.body.decode('utf-8')
    parsed = urlparse(raw_body)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = raw_body
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
