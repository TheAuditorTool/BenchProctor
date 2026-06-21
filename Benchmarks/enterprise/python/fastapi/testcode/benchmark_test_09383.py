# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09383(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
