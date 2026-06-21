# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47648(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
