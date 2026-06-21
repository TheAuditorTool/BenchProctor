# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62355(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
