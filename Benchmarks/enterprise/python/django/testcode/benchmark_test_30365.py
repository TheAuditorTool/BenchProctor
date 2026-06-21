# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket


def BenchmarkTest30365(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = json_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
