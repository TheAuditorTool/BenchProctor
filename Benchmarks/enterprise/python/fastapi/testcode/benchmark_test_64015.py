# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64015(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        result = int(str(ua_value))
    except Exception:
        pass
    return {"updated": True}
