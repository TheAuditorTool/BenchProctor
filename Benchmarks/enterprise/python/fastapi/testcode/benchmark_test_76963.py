# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76963(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
