# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03991(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
