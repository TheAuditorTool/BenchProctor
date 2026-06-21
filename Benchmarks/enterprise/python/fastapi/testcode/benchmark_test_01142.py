# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01142(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
