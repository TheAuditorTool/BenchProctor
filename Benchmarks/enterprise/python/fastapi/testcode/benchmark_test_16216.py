# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16216(request: Request):
    referer_value = request.headers.get('referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return {"updated": True}
