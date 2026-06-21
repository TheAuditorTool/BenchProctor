# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest45215(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
