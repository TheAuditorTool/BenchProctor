# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71895(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
