# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60084(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
