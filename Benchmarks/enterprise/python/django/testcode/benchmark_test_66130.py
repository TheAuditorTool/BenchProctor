# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket
import os


def BenchmarkTest66130(request):
    env_value = os.environ.get('USER_INPUT', '')
    parsed = urlparse(env_value)
    resolved = socket.gethostbyname(parsed.hostname or env_value)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = env_value.replace(parsed.hostname, resolved) if parsed.hostname else env_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
