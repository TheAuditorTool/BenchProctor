# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket


def BenchmarkTest33321(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parsed = urlparse(forwarded_ip)
    resolved = socket.gethostbyname(parsed.hostname or forwarded_ip)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = forwarded_ip.replace(parsed.hostname, resolved) if parsed.hostname else forwarded_ip
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
