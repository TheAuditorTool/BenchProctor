# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53909(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
