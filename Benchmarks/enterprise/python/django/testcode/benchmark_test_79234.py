# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket


def BenchmarkTest79234(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parsed = urlparse(referer_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = referer_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
