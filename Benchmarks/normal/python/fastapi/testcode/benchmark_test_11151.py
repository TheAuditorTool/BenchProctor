# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11151(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
