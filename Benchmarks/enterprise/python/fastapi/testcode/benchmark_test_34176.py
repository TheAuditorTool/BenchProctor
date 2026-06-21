# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34176(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ' '.join(str(forwarded_ip).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
