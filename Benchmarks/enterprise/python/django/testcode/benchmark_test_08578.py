# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest08578(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parsed = urlparse(header_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = header_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
