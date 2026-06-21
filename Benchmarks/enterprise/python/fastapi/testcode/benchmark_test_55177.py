# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55177(request: Request):
    auth_header = request.headers.get('authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
