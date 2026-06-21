# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07302(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
