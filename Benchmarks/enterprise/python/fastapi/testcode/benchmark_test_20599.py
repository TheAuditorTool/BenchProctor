# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20599(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
