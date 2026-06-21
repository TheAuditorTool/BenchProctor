# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78719(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = RequestPayload(forwarded_ip).value
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
