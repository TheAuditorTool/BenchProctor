# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50981(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(raw_body))
    return {"updated": True}
