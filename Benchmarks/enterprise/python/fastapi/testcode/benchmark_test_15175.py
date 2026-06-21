# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest15175(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
