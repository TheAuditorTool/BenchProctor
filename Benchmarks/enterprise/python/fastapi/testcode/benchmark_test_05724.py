# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05724(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
