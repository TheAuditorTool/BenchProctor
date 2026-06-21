# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75770(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    result = 100 / int(str(data))
    return {"updated": True}
