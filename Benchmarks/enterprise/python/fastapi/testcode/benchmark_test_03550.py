# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse


async def BenchmarkTest03550(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
