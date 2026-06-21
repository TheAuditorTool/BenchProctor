# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
import ipaddress
import socket
from starlette.responses import JSONResponse
import json


async def BenchmarkTest80634(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parsed = urlparse(graphql_var)
    resolved = socket.gethostbyname(parsed.hostname or graphql_var)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = graphql_var.replace(parsed.hostname, resolved) if parsed.hostname else graphql_var
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
