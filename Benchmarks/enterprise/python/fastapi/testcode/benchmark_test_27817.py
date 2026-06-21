# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27817(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return {"updated": True}
