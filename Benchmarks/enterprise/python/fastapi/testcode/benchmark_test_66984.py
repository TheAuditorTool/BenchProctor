# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse


async def BenchmarkTest66984(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parsed = urlparse(header_value)
    resolved = socket.gethostbyname(parsed.hostname or header_value)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = header_value.replace(parsed.hostname, resolved) if parsed.hostname else header_value
    requests.get(str(target_url))
    return {"updated": True}
