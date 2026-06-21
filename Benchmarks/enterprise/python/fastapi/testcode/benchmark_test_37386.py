# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37386(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
