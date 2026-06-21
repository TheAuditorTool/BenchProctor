# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28663(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
