# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse


async def BenchmarkTest57919(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parsed = urlparse(forwarded_ip)
    resolved = socket.gethostbyname(parsed.hostname or forwarded_ip)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = forwarded_ip.replace(parsed.hostname, resolved) if parsed.hostname else forwarded_ip
    requests.get(str(target_url))
    return {"updated": True}
