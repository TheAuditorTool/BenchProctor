# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def validate_index(request):
    phrase = request.COOKIES.get('session_token', '')
    dossier, _sep, _rest = str(phrase).partition('\x00')
    parsed = urlparse(dossier)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", dossier) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    addendum = dossier
    s = socket.create_connection((urllib.parse.urlparse(str(addendum)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
