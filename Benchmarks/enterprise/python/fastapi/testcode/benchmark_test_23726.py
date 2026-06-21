# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23726(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
