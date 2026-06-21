# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest59120(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return {"updated": True}
