# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60333(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        result = int(str(referer_value))
    except Exception:
        pass
    return {"updated": True}
