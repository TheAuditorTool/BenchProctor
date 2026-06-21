# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34442(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
