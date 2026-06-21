# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45150(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
