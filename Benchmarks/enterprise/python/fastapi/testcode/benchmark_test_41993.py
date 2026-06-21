# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41993(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
