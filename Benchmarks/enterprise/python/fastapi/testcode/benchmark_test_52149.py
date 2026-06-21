# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest52149(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
