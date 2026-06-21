# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest03201(request):
    xml_value = request.body.decode('utf-8')
    parsed = urlparse(xml_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = xml_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
