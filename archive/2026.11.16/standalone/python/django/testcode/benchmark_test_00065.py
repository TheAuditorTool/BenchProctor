# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import requests
import socket
import re


def BenchmarkTest00065(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data, _sep, _rest = str(api_value).partition('\x00')
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
