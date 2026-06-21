# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest78167(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    s = socket.create_connection((str(forwarded_ip), 80))
    s.close()
    return {"updated": True}
