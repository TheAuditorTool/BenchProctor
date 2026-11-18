# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def score_anomaly(request):
    citation = json.loads(request.body or b'{}').get("telemetry_payload", "")
    parsed = urlparse(citation)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    gauge = citation
    s = socket.create_connection((str(gauge), 80))
    s.close()
    return JsonResponse({"saved": True})
