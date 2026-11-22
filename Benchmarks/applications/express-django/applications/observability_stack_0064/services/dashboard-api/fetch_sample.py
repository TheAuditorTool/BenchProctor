# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def fetch_sample(request):
    tagline = request.META.get('HTTP_ORIGIN', '')
    gauge = (lambda v: v.strip())(tagline)
    parsed = urlparse(gauge)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", gauge) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    cohort = gauge
    s = socket.create_connection((urllib.parse.urlparse(str(cohort)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
