# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40184(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
