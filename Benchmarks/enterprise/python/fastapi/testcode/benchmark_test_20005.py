# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20005(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
