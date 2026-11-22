# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def archive_ledger(request):
    tagline = request.META.get('HTTP_ORIGIN', '')
    persona = (lambda v: v.strip())(tagline)
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    note = persona
    s = socket.create_connection((urllib.parse.urlparse(str(note)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
