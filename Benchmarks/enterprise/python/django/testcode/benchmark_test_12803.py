# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket


def BenchmarkTest12803(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parsed = urlparse(header_value)
    resolved = socket.gethostbyname(parsed.hostname or header_value)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = header_value.replace(parsed.hostname, resolved) if parsed.hostname else header_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
