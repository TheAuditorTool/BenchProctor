# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest11035(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parsed = urlparse(auth_header)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = auth_header
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
