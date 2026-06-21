# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34623(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return {"updated": True}
