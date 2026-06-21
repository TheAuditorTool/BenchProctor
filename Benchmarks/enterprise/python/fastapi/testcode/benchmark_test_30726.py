# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30726(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
