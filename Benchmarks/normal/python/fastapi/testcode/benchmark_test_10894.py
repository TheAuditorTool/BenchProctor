# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse


async def BenchmarkTest10894(request: Request):
    origin_value = request.headers.get('origin', '')
    parsed = urlparse(origin_value)
    resolved = socket.gethostbyname(parsed.hostname or origin_value)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = origin_value.replace(parsed.hostname, resolved) if parsed.hostname else origin_value
    requests.get(str(target_url))
    return {"updated": True}
