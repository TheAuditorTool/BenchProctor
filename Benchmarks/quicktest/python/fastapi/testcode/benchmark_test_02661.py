# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest02661(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
