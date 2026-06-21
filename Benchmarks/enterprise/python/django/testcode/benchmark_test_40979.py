# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest40979(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
