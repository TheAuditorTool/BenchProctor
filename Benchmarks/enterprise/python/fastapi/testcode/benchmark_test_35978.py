# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35978(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
