# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35673(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
