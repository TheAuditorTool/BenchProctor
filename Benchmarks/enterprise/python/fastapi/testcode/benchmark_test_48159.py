# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48159(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
