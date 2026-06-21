# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04858(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
