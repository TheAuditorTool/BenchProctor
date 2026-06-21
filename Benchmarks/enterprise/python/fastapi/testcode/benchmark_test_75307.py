# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75307(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
