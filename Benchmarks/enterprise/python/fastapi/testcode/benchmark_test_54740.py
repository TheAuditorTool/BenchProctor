# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54740(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
