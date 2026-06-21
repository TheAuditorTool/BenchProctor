# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38242(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
