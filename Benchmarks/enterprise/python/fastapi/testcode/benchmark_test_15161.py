# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15161(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
