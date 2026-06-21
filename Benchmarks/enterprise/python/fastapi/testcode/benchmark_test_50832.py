# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50832(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    int(str(data))
    return {"updated": True}
