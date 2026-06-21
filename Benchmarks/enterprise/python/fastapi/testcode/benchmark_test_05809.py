# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05809(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    int(str(data))
    return {"updated": True}
