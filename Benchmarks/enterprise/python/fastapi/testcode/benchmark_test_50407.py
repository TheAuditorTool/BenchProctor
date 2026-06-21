# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50407(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    result = 100 / int(str(data))
    return {"updated": True}
