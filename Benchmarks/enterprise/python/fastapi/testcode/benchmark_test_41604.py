# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41604(request: Request):
    host_value = request.headers.get('host', '')
    size = min(int(host_value) if str(host_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
