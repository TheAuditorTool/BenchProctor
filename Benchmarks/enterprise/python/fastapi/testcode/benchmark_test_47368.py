# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47368(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    result = 100 / int(str(data))
    return {"updated": True}
