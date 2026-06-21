# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19103(request: Request):
    host_value = request.headers.get('host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['data'] = str(data)
    return {"updated": True}
