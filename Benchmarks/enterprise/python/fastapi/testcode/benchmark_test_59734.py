# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59734(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    int(str(forwarded_ip))
    return {"updated": True}
