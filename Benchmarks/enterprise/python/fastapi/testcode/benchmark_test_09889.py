# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09889(request: Request):
    origin_value = request.headers.get('origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return {"updated": True}
