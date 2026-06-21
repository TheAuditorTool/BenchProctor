# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58678(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
