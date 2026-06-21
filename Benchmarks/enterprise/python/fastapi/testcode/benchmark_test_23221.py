# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23221(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
