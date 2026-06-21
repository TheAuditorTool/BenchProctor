# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest20150(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
