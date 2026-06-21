# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26565(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
