# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43111(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
