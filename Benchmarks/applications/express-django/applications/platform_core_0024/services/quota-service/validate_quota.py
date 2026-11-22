# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def validate_quota(request):
    heading = request.COOKIES.get('session_token', '')
    handshake, _sep, _rest = str(heading).partition('\x00')
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    persona = handshake
    s = socket.create_connection((urllib.parse.urlparse(str(persona)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
