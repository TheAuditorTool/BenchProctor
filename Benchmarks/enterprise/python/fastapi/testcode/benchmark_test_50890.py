# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50890(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    result = 100 / int(str(data))
    return {"updated": True}
