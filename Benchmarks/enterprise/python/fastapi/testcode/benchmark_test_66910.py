# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66910(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
