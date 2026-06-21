# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket


async def BenchmarkTest69705(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
