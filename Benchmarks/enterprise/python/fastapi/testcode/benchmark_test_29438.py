# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29438(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
