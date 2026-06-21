# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest28337(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
