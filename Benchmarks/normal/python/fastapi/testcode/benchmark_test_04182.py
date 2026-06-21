# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04182(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
