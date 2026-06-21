# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import socket


async def BenchmarkTest52555(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
