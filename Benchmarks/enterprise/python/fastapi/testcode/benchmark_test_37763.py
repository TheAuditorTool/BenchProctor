# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37763(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
