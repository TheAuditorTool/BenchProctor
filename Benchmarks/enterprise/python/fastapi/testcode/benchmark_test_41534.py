# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41534(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    eval(str(data))
    return {"updated": True}
