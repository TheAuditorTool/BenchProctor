# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55770(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(forwarded_ip) + ',data\n')
    return {"updated": True}
