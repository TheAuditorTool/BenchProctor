# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import ipaddress
import socket
import json


def BenchmarkTest19195(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parsed = urlparse(graphql_var)
    resolved = socket.gethostbyname(parsed.hostname or graphql_var)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = graphql_var.replace(parsed.hostname, resolved) if parsed.hostname else graphql_var
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
