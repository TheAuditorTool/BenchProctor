# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket


def BenchmarkTest50486(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parsed = urlparse(header_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = header_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
