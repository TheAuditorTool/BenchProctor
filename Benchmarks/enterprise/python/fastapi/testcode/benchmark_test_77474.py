# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77474(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
