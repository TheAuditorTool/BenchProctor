# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33480(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
