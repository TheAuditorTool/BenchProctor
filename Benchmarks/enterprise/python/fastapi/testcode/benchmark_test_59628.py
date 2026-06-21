# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59628(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    int(str(data))
    return {"updated": True}
