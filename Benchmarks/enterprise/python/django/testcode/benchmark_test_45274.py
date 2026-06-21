# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from types import SimpleNamespace
from app_runtime import mq_client


def BenchmarkTest45274(request):
    msg_value = mq_client.get_message().body
    ns = SimpleNamespace(payload=msg_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
