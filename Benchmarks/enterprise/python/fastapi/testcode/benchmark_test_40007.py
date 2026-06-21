# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest40007(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
