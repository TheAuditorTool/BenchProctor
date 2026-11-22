# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import re


@csrf_exempt
def archive_checkpoint(request):
    subtitle = request.META.get('HTTP_AUTHORIZATION', '')
    persona = bytes.fromhex(subtitle).decode('utf-8', 'ignore')
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    handshake = persona
    outbound = urllib.request.Request(str(handshake), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
