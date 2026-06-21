# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30217(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
