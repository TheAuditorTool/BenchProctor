# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38771(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
