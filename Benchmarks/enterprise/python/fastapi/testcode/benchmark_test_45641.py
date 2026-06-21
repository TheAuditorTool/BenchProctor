# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45641(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
