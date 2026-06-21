# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import ipaddress
import socket
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest34953(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
