# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import socket
import json
import re


def BenchmarkTest00633(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
