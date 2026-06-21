# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39025(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
