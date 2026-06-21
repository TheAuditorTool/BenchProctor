# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33137(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
