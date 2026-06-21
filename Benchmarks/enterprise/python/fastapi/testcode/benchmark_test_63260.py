# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63260(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
