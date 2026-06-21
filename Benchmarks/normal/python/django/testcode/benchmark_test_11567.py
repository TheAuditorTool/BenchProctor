# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest11567(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
