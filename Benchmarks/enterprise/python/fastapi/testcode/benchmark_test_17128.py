# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17128(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
