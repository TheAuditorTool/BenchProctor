# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28739(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
