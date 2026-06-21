# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01215(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
