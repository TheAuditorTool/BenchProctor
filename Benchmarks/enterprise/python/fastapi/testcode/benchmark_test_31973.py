# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31973(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
