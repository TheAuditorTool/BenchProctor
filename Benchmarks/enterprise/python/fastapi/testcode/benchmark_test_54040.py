# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54040(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    exec(str(data))
    return {"updated": True}
