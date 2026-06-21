# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest10524(request: Request, field: str = Form('')):
    field_value = field
    parsed = urlparse(field_value)
    resolved = socket.gethostbyname(parsed.hostname or field_value)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = field_value.replace(parsed.hostname, resolved) if parsed.hostname else field_value
    requests.get(str(target_url))
    return {"updated": True}
