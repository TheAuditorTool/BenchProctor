# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75703(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
