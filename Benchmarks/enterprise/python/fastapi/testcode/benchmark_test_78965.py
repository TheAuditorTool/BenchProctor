# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78965(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    eval(str(data))
    return {"updated": True}
