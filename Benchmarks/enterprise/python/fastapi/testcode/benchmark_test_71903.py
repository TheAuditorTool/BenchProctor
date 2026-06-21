# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
import ipaddress
import socket
from pydantic import BaseModel
from starlette.responses import JSONResponse
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest71903(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
