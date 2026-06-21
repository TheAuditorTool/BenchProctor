# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37468(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
