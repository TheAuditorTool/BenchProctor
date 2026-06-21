# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26403(request: Request):
    auth_header = request.headers.get('authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return {"updated": True}
