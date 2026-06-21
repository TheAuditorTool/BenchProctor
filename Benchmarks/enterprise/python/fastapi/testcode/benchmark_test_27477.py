# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27477(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    request.session['data'] = str(data)
    return {"updated": True}
