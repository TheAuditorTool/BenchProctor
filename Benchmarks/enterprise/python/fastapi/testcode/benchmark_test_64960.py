# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64960(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
