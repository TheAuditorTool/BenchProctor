# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket


def BenchmarkTest12672(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parsed = urlparse(origin_value)
    resolved = socket.gethostbyname(parsed.hostname or origin_value)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = origin_value.replace(parsed.hostname, resolved) if parsed.hostname else origin_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
