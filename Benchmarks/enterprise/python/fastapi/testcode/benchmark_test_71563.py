# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71563(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    eval(str(data))
    return {"updated": True}
