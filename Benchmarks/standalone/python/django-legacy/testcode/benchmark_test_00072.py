# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


def BenchmarkTest00072(request):
    cookie_value = request.COOKIES.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((urllib.parse.urlparse(str(target_url)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
