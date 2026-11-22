# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import urllib.parse
import re


@csrf_exempt
def configure_sample(request):
    blurb = json.loads(request.body or b'{}').get("telemetry_payload", "")
    parsed = urlparse(blurb)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", blurb) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    cohort = blurb
    s = socket.create_connection((urllib.parse.urlparse(str(cohort)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
