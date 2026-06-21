# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28360(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
