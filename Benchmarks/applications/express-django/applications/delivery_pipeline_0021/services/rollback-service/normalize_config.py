# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def normalize_config(request):
    summary = request.COOKIES.get('session_token', '')
    phrase, _sep, _rest = str(summary).partition('\x00')
    parsed = urlparse(phrase)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", phrase) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    subtitle = phrase
    s = socket.create_connection((urllib.parse.urlparse(str(subtitle)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
