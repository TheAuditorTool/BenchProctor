# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41828(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
