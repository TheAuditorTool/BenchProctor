# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76364(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
