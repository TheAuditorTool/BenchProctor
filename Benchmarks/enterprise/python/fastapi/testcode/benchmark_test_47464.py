# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47464(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
