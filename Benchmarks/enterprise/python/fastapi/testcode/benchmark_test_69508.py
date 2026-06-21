# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69508(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
