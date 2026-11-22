# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def publish_summary(request):
    headline = request.COOKIES.get('session_token', '')
    disbursement, _sep, _rest = str(headline).partition('\x00')
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    remittance = disbursement
    s = socket.create_connection((urllib.parse.urlparse(str(remittance)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
