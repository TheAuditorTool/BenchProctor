# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66449(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
