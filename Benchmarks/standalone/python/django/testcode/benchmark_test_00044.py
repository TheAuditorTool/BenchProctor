# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


def BenchmarkTest00044(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
